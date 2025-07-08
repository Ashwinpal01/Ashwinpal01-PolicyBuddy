import streamlit as st
import pdfplumber
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load API key
load_dotenv()
import streamlit as st
import os

api_key = st.secrets["OPENROUTER_API_KEY"]


# Set up OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Streamlit Page Config
st.set_page_config(page_title="PolicyBuddy", layout="centered")

# --- Custom Light UI Styling ---
st.markdown(
    """
    <style>
    html, body, .main, .stApp {
        background-color: #fafafa;
        color: #1e1e1e;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextInput > div > input,
    .stTextArea > div > textarea,
    .stFileUploader,
    .stSelectbox div {
        background-color: #ffffff;
        color: #1e1e1e;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 0.4rem;
    }
    .stButton button {
        background-color: #f0f0f0;
        color: #1e1e1e;
        border: 1px solid #ccc;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .stButton button:hover {
        background-color: #e0e0e0;
    }
    .stFileUploader > div {
        border: 2px dashed #bbb;
        background-color: #f9f9f9;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Main Header ---
st.markdown("### 📜 **PolicyBuddy**")
st.markdown("#### Understand Government Policies – Simply")

# --- Input Section ---
uploaded_file = st.file_uploader("📎 Upload a government policy (PDF)", type="pdf")

col1, col2 = st.columns(2)
with col1:
    role = st.text_input("👤 Your role", placeholder="e.g. student, farmer, business owner")
with col2:
    location = st.text_input("📍 Your location", placeholder="e.g. Delhi, California")

# --- Function to extract text from PDF ---
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

# --- Function to summarize policy using LLM ---
def summarize_policy(text, role, location):
    prompt = f"""You are a helpful assistant. Explain this government policy in simple terms for a person who is a {role} in {location}.

    POLICY DOCUMENT:
    {text[:3000]}
    """
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",
        extra_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "PolicyBuddy",
        },
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content

# --- Output ---
if uploaded_file and role and location:
    with st.spinner("🔍 Reading and analyzing your policy..."):
        text = extract_text_from_pdf(uploaded_file)
        result = summarize_policy(text, role, location)
        st.success("✅ Here's a simplified explanation:")
        st.write(result)

st.markdown("---")
st.caption("⚠️ This is an AI-generated explanation and not official legal advice.")
