import os
from dotenv import load_dotenv                      # To load env variables
from fastapi import FastAPI, Request                # To create a web server
import httpx                                        # To make API requests
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI             # To connect bot to OpenAI for AI reviews

# Load .env file variables into environment
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Create a web server to listen to webhooks
app = FastAPI()

# Initializing GPT-4o-mini model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    if payload.get("action") == "opened":
        pr_number = payload["pull_request"]["number"]
        repo = payload["repository"]["full_name"]

        # Fetch PR files
        files_changed = await get_pr_files(repo, pr_number)
        print("Files Changed:", files_changed)

        # Analyze Code
        review_comments = await analyze_code(files_changed)

        # Post AI-generated review comments on PR
        all_comments = "\n\n".join([
            f"### File: `{file}`\n" + "\n".join(suggestions)
            for file, suggestions in review_comments.items()
        ])

        if all_comments:
            await comment_on_pr(repo, pr_number, f"## Suggested Improvements\n\n{all_comments}")

            return {"message": "Webhook received"}

async def get_pr_files(repo: str, pr_number: int):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code != 200:
        print(f"GitHub API Error: {response.status_code} - {response.text}")
        return []

    return response.json()

async def analyze_code(files_changed):
    review_comments = {}

    for file in files_changed:
        file_name = file["filename"]
        patch = file.get("patch", "")

        if patch:
            prompt = f"Review this code and suggest improvements:\n{patch}"
            response = await llm.agenerate([[HumanMessage(content=prompt)]])
            print(f"AI Review for {file_name}:", response.generations[0][0].text)

            review_comments[file_name] = response.generations[0][0].text.split("\n")

    return review_comments

async def comment_on_pr(repo: str, pr_number: int, comment: str):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {"body": comment}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print(f"Successfully commented on PR #{pr_number}")
    else:
        print(f"Failed to comment: {response.status_code} - {response.text}")
