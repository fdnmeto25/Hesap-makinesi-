import streamlit as st
import random

st.title("Tahmin Oyunu")

if 'sayi' not in st.session_state:
    st.session_state.sayi = random.randint(1, 100)

tahmin = st.number_input("Tahminini gir", min_value=1, max_value=100)

if st.button("Kontrol Et"):
    if tahmin < st.session_state.sayi:
        st.write("Daha büyük bir sayı gir!")
    elif tahmin > st.session_state.sayi:
        st.write("Daha küçük bir sayı gir!")
    else:
        st.write("Tebrikler, bildin!")
      
