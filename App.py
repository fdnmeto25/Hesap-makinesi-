import streamlit as st
import google.generativeai as genai
AQ.Ab8RN6KKpx7l6KjCZOK13sui3YoF5B5cAJ1lhUwKZ62BSjAvnw
# Anahtarın güncellendi
genai.configure(api_key="AQ.Ab8RN6KKpx7l6KjCZOK13sui3YoF5B5cAJ1lhUwKZ62BSjAvnw")

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Metehan'ın Kişisel Asistanı")

soru = st.text_input("Bana bir şey sor:")

if st.button("Sor"):
    if soru:
        try:
            cevap = model.generate_content(soru)
            st.write(cevap.text)
        except Exception as e:
            st.write("Bir hata oluştu. Lütfen Google AI Studio'dan 'AIza' ile başlayan bir anahtar oluşturduğundan emin ol.")
            st.write("Hata detayı: " + str(e))
            
