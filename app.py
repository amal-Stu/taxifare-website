import streamlit as st
import streamlit as st

st.title("🏢 Building Floors Printer")

floor_count = st.number_input("How many floors do you want to print?", min_value=1, max_value=100, value=5)

if st.button("Print Floors"):
    st.write("### List of Floors:")
    for i in range(1, floor_count + 1):
        st.write(f"🟫 Floor Number {i}")
