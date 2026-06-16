import streamlit as st
import random

st.title("Metehan'ın Tahmin Ustası")

if 'sayi' not in st.session_state:
    st.session_state.sayi = random.randint(1, 100)

tahmin = st.number_input("Tahminini gir (1-100):", min_value=1, max_value=100)

if st.button("Kontrol Et"):
    if tahmin < st.session_state.sayi:
        st.write("Daha büyük bir sayı gir!")
    elif tahmin > st.session_state.sayi:
        st.write("Daha küçük bir sayı gir!")
    else:
        st.success("Tebrikler! Doğru bildin!")
        if st.button("Yeniden Başla"):
            st.session_state.sayi = random.randint(1, 100)
            st.rerun()
          
