# import streamlit as st
import random

st.title("🎯 Sayı Tahmin Ustası - Pro")

if 'sayi' not in st.session_state:
    st.session_state.sayi = random.randint(1, 100)
    st.session_state.sayac = 0

tahmin = st.number_input("Tahminini gir (1-100):", min_value=1, max_value=100)

if st.button("Kontrol Et"):
    st.session_state.sayac += 1
    if tahmin < st.session_state.sayi:
        st.warning("Daha büyük bir sayı gir!")
    elif tahmin > st.session_state.sayi:
        st.warning("Daha küçük bir sayı gir!")
    else:
        st.success(f"Tebrikler! {st.session_state.sayac}. denemede buldun.")
        st.balloons()
        if st.button("Yeniden Başla"):
            st.session_state.sayi = random.randint(1, 100)
            st.session_state.sayac = 0
            st.rerun()

st.write(f"Şu ana kadar {st.session_state.sayac} tahmin yaptın.")
