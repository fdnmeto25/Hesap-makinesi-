import streamlit as st
import google.generativeai as genai

# Anahtarını buraya yapıştır
genai.configure(api_key="AIza.Ab8RN6Jb3cYSOygOD3aQG1fjNJ0JnfhYhYrPd5bJfyzloHCN8w")

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Metehan'ın Kişisel Asistanı")

soru = st.text_input("Bana bir şey sor:")

if st.button("Sor"):
    if soru:
        cevap = model.generate_content(soru)
        st.write(cevap.text)


