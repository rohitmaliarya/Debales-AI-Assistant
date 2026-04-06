from langgraph.graph import StateGraph
from rag import load_rag
from tools import search_google
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    task="text2text-generation",
    model_kwargs={
        "temperature": 0.7,
        "max_length": 512
    }
)
retriever = load_rag()

# ✅ Router function
def route(state):
    question = state.get("question", "").lower()

    debales_keywords = ["debales", "ai assistant", "automation", "workflow"]

    # If question is about Debales
    if any(k in question for k in debales_keywords):
        return "rag"
    else:
        # Non-Debales → Use SERP
        return "search"

# ✅ Router node
def router_node(state):
    return {"question": state["question"]}


# ✅ RAG node
def rag_node(state):
    question = state["question"]
    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question using ONLY the context below.

If the answer is not in the context, say:
"I don't have relevant information."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return {"context": response}   # ✅ return context, not answer

    return {"answer": response.content}
# ✅ Search node
def search_node(state):
    question = state.get("question", "")
    result = search_google(question)

    return {"context": str(result)}   # ✅ correct
# ✅ BOTH node
def both_node(state):
    question = state.get("question", "")

    rag_result = rag_node(state)["context"]
    search_result = search_google(question)

    return {
        "context": f"{rag_result}\n\nAdditional Info: {search_result}"
    }

# ✅ Final node (no hallucination)
def final_node(state):
    context = state.get("context", "").strip()

    if not context or len(context) < 20:
        return {"answer": "Sorry, I could not find relevant information."}

    # Return full context, no truncation
    return {"answer": context}
def classify_question(question):
    question = question.lower()

    debales_keywords = ["debales", "ai assistant", "automation", "workflow"]

    if any(k in question for k in debales_keywords):
        return "rag"
    else:
        return "serp"
# ✅ BUILD GRAPH (FIXED)
def build_graph():

    graph = StateGraph(dict)   # 🔥 IMPORTANT

    graph.add_node("router", router_node)
    graph.add_node("rag", rag_node)
    graph.add_node("search", search_node)
    graph.add_node("both", both_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        route,
        {
            "rag": "rag",
            "search": "search",
            "both": "both"
        }
    )

    graph.add_edge("rag", "final")
    graph.add_edge("search", "final")
    graph.add_edge("both", "final")

    return graph.compile()