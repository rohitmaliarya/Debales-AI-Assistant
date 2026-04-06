from graph import build_graph
from dotenv import load_dotenv

load_dotenv()

print("🚀 Debales AI Assistant Started (type 'exit' to quit)\n")

app = build_graph()

while True:
    try:
        query = input("Ask: ")

        if query.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        result = app.invoke({"question": query})

        print("\nAnswer:", result.get("answer", "No answer found"))

    except Exception as e:
        print("Error:", e)