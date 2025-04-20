import streamlit as st

st.title("🏢 طباعة أدوار المبنى")

floor_count = st.number_input("كم دور تبغى تطبع؟", min_value=1, max_value=100, value=5)

if st.button("اطبع الأدوار"):
    st.write("### قائمة الأدوار:")
    for i in range(1, floor_count + 1):
        st.write(f"🟫 الدور رقم {i}")
