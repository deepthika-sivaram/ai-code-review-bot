# 🚀 AI-Powered GitHub Code Review Bot 

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)  
[![LangChain](https://img.shields.io/badge/LangChain-0.2.0-blue)](https://python.langchain.com/)  
[![GitHub API](https://img.shields.io/badge/GitHub%20API-v3-blueviolet)](https://docs.github.com/en/rest)  
[![OpenAI API](https://img.shields.io/badge/OpenAI%20API-GPT--4o-orange)](https://platform.openai.com/docs/)  

## **📝 Overview**
This **GitHub bot** automatically **reviews Pull Requests (PRs)** using **AI (GPT-4o-mini)** and **comments on GitHub with suggested improvements**. It integrates **FastAPI**, **GitHub Webhooks**, and **OpenAI API** to streamline **code reviews**.

## **✨ Features**
✅ **Listens to GitHub Webhooks** for new PRs  
✅ **Fetches PR file changes** using GitHub API  
✅ **Analyzes code** using OpenAI GPT models  
✅ **Posts AI-generated feedback** directly as PR comments  
✅ **Formats comments with Markdown & emojis** for better readability  

---

## **🛠 Tech Stack**
- **Backend:** `FastAPI`, `Python 3.x`
- **AI Model:** `OpenAI GPT-4o-mini` (via `LangChain`)
- **Webhooks & APIs:** `GitHub API`, `httpx`
- **Async Processing:** `asyncio`, `httpx.AsyncClient`

---

## **📦 Installation & Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-code-review-bot.git
   cd ai-code-review-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up .env (API keys):
   ```bash
   OPENAI_API_KEY=your-openai-key
   GITHUB_TOKEN=your-github-token
   ```
   You can generate your Github Token from Settings > Developer Settings > Personal Access Tokens > Generate new token (Generate with repo access)
   For OpenAI API Key, login to OpenAI, make sure you have billing credits available for API requests and response. Then API Keys > Generate API Key
6. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   Your API will be live at:
  📍 http://127.0.0.1:8000/webhook

## 🔗 Setting Up GitHub Webhooks
To connect the bot to GitHub:
1️⃣ Go to your GitHub Repo → Settings → Webhooks
2️⃣ Click "Add Webhook"
3️⃣ Payload URL: http://your-server-url/webhook (server-url from ngrok)
4️⃣ Content type: application/json
5️⃣ Trigger: Select Pull Request events
6️⃣ Click Save

✅ Now, your bot will automatically review PRs!

## 📜 Example AI-Generated Comment
Once a PR is opened, the bot posts structured feedback like this:
<img width="1058" alt="image" src="https://github.com/user-attachments/assets/36d5ce61-1efd-4120-9997-7afefa65be07" />


## 🚀 Deployment Options
🔹 Using Ngrok (For Local Testing)
  ```bash
  ngrok http 8000
  ```
  Then update your webhook URL with the Ngrok-generated public URL.

🔹 Cloud Deployment
  Render: https://render.com/
  Railway.app: https://railway.app/
  AWS Lambda (for serverless)
  
## 📌 Future Enhancements
✅ Support for multiple programming languages
✅ Ability to fine-tune AI suggestions based on project type
✅ Custom rule-based linting with AI feedback
✅ Webhook security using HMAC validation

## 🛠 Contributing
Contributions are welcome! Feel free to:
  Fork the repository 🍴
  Create a feature branch (git checkout -b feature-new)
  Submit a Pull Request ✅
