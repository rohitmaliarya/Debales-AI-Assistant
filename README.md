# 🤖 Debales AI Assistant (RAG + Tool Calling + LangGraph)

## 🚀 Overview

Debales AI Assistant is a hybrid chatbot that intelligently answers user queries by combining:

* 📚 **RAG (Retrieval-Augmented Generation)** for Debales-specific knowledge
* 🌐 **SERP API (Google Search)** for general queries
* 🔀 **LangGraph workflow** for dynamic routing

The system ensures **accurate, context-aware responses** while preventing hallucinations.

---

## 🧠 Features

* ✅ **RAG-based Question Answering**

  * Uses scraped data from Debales website, blogs, and product pages
  * Retrieves relevant context using vector embeddings

* ✅ **Tool Calling (SERP API)**

  * Fetches real-time information for non-Debales queries
  * Uses Google Search API (SerpAPI)

* ✅ **Hybrid Query Handling**

  * Debales queries → RAG
  * General queries → SERP API
  * Mixed queries → BOTH

* ✅ **LangGraph Workflow**

  * Intelligent routing between RAG and search tools

* ✅ **No Hallucination**

  * Returns safe fallback when no reliable data is found

---

## 🏗️ Architecture

```
User Query
   ↓
LangGraph Router
   ↓
 ┌───────────────┬───────────────┬───────────────┐
 │ RAG           │ SERP API      │ BOTH          │
 │ (Debales)     │ (General)     │ (Mixed)       │
 └───────────────┴───────────────┴───────────────┘
   ↓
Final Clean Response
```

---

## ⚙️ Tech Stack

* **Python**
* **LangChain**
* **LangGraph**
* **FAISS / Vector DB**
* **SerpAPI (Google Search API)**
* **Requests**
* **dotenv**

---

## 📂 Project Structure

```
├── main.py          # CLI chatbot
├── graph.py         # LangGraph workflow
├── rag.py           # RAG setup (vector store + retriever)
├── tools.py         # SERP API integration
├── .env             # API keys
└── data/            # Scraped Debales content
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/debales-ai-assistant.git
cd debales-ai-assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Key

Create `.env` file:

```
SERP_API_KEY=your_api_key_here
```

### 4️⃣ Run the Chatbot

```bash
python main.py
```

---

## 💬 Example Usage

### ✅ Debales Query (RAG)

```
Ask: What is Debales AI?
Answer: Debales AI is an AI-powered platform that automates business operations...
```

### ✅ General Query (Search)

```
Ask: Who is Virat Kohli?
Answer: Virat Kohli is an Indian international cricketer...
```

### ✅ Mixed Query (Hybrid)

```
Ask: What is Debales AI and who uses it?
Answer:
Debales AI is an AI-powered platform...

Additional Info: It is used by businesses...
```

### ✅ Unknown Query (No Hallucination)

```
Ask: random xyz 123
Answer: Sorry, I could not find relevant information.
```

---

## 🧪 Testing Strategy

* ✔ Verified routing logic (RAG / Search / Both)
* ✔ Tested edge cases (unknown queries)
* ✔ Ensured no hallucinated responses

---

## 🎯 Key Learnings

* Building **hybrid AI systems (RAG + APIs)**
* Designing **LangGraph workflows**
* Implementing **tool calling in LLM pipelines**
* Handling **hallucination and response validation**

---

## 📌 Future Improvements

* 🌐 Add Streamlit UI
* 🧠 Use LLM for better summarization
* 🔍 Semantic routing using embeddings
* 📊 Logging & analytics

---

## 👨‍💻 Author

**Rohit Mali**

* 💡 AI/ML Enthusiast
* 🔐 Cybersecurity Learner
* 🚀 Aspiring AI Engineer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
