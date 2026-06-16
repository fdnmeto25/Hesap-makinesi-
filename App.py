import streamlit as st
import google.generativeai as genai

# API anahtarını buraya ekleyeceksin
genai.configure(api_key="BURAYA_API_ANAHTARINI_YAZ")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Metehan'ın Kişisel Asistanı")

soru = st.text_input("Bana bir şey sor:")

if st.button("Sor"):
    if soru:
        cevap = model.generate_content(soru)
        st.write(cevap.text)
        
