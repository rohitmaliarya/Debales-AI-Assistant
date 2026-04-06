import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_google(query):
    import os
    import requests

    api_key = os.getenv("SERP_API_KEY")

    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": api_key}

    res = requests.get(url, params=params)
    data = res.json()

    # ✅ Answer box
    if "answer_box" in data:
        box = data["answer_box"]
        return box.get("answer") or box.get("snippet")

    # ✅ Knowledge graph
    if "knowledge_graph" in data:
        kg = data["knowledge_graph"]
        return f"{kg.get('title')} - {kg.get('description')}"

    # ✅ Organic results with FILTER 🔥
    if "organic_results" in data:
        snippet = data["organic_results"][0].get("snippet", "").lower()

        # ❌ Detect garbage / low-quality results
        bad_keywords = [
            "spotify", "instagram", "followers", "songs",
            "playlist", "watch", "download", "login"
        ]

        if any(word in snippet for word in bad_keywords):
            return ""   # 🔥 force no result

        return snippet

    return ""