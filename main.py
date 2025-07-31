
import streamlit as st
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
ULTRAMSG_INSTANCE_ID = os.getenv("ULTRAMSG_INSTANCE_ID")
ULTRAMSG_TOKEN = os.getenv("ULTRAMSG_TOKEN")

# Sample user profiles
girls = [
    {"name": "Nimra", "age": 28, "city": "Faisalabad", "profession": "AI Research Engineer"},
    {"name": "Iqra", "age": 21, "city": "Multan", "profession": "Prompt Engineer"},
    {"name": "Areeba", "age": 23, "city": "Quetta", "profession": "Data Scientist"},
    {"name": "Hira", "age": 20, "city": "Sialkot", "profession": "Conversational AI Specialist"}
]

boys = [
    {"name": "Aliyar", "age": 22, "city": "Karachi", "profession": "Agentic AI Developer"},
    {"name": "Shaz", "age": 25, "city": "Lahore", "profession": "Agentic AI Developer"},
    {"name": "Hasan", "age": 19, "city": "Islamabad", "profession": "Agentic AI Developer"},
    {"name": "Taha", "age": 24, "city": "Peshawar", "profession": "Machine Learning Scientist"},
    {"name": "Zain", "age": 26, "city": "Hyderabad", "profession": "AI Product Manager"},
    {"name": "Saad", "age": 27, "city": "Rawalpindi", "profession": "NLP Engineer"}
]

# WhatsApp sender
def send_whatsapp_message(number: str, message: str) -> str:
    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"
    payload = {"token": ULTRAMSG_TOKEN, "to": number, "body": message}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return f"✅ Rishta details sent to WhatsApp: {number}"
    else:
        return f"❌ Failed to send. Error: {response.text}"

# Streamlit UI
st.set_page_config(page_title="Rishty Wali Aunty", page_icon="💍")
st.title(" Rishty Wali Aunty " \
"AI Rishta Finder")
st.markdown("Type what you're looking for — e.g., *Looking for a bride* or *Need a groom*.")

with st.form("match_form"):
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=18, max_value=100, step=1)
    prompt = st.text_input("What are you looking for?")
    whatsapp = st.text_input("Your WhatsApp Number (optional)", placeholder="+923001234567")
    submitted = st.form_submit_button("Find Matches")

# 🛠️ FIXED: Correct matching logic
def detect_interest(text):
    text = text.lower()
    if "groom" in text or "larka" in text or "boy" in text or "husband" in text or "male" in text:
        return "boy"   # user needs a boy => show boys
    elif "bride" in text or "larki" in text or "girl" in text or "wife" in text or "female" in text:
        return "girl"  # user needs a girl => show girls
    return "unknown"

if submitted:
    interest = detect_interest(prompt)
    st.success(f"Hi {name}, searching matches for you...")

    if interest == "boy":
        st.subheader("🎯 Suitable Grooms for You:")
        matches = boys
    elif interest == "girl":
        st.subheader("🎯 Suitable Brides for You:")
        matches = girls
    else:
        st.warning("❗ Please clearly mention 'bride' or 'groom' in the prompt.")
        matches = []

    # Display profiles and send to WhatsApp
    message_text = f"Assalamualaikum {name}!\nHere are your rishta matches:\n\n"
    for match in matches:
        profile = f"• Name: {match['name']}, Age: {match['age']}, City: {match['city']}, Profession: {match['profession']}"
        st.markdown(f"""
        - **Name**: {match['name']}
        - **Age**: {match['age']}
        - **City**: {match['city']}
        - **Profession**: {match['profession']}
        """)
        st.markdown("---")
        message_text += profile + "\n"

    if whatsapp.strip() and matches:
        result = send_whatsapp_message(whatsapp.strip(), message_text)
        st.info(result)



















































































































