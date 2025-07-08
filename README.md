# 📜 PolicyBuddy – Understand Government Policies Easily

**PolicyBuddy** is a lightweight, GenAI-powered Streamlit app designed to help citizens understand complex government policy documents in simple, human-readable language. Upload a PDF of any official policy, specify your role and location, and let PolicyBuddy summarize the content using advanced language models like DeepSeek/Qwen via OpenRouter.

---

## 🚀 Features

- 📂 **PDF Upload** – Upload any government policy in PDF format
- 🧠 **AI-Powered Summarization** – Uses OpenRouter (e.g. DeepSeek/Qwen) to generate simple explanations
- 🧍‍♂️ **Role-Based Personalization** – Tailors responses for students, farmers, business owners, etc.
- 📍 **Location Awareness** – Provides summaries relevant to your location
- 🧑‍💻 **Clean, Responsive UI** – Streamlit-based minimal interface with a smooth user experience
- 🔐 **Secure API Key Handling** – Keys are managed through Streamlit Secrets (not pushed in the repo)

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **GenAI Model**: OpenRouter (DeepSeek)
- **PDF Parsing**: `pdfplumber`
- **Environment**: `.env` (for local dev) and `st.secrets` (for Streamlit Cloud)
