import streamlit as st

st.set_page_config(page_title="Crop Advisor")

st.title("🌱 Crop Advisor")

tab1, tab2, tab3 = st.tabs([
    "Quick Ask",
    "Guided Diagnosis",
    "Soil Report Analysis"
])

with tab1:
    st.header("Quick Ask")
    question = st.text_input("Ask an agricultural question")

    if question:
       st.write("You asked:", question)

with tab2:
    st.header("Guided Diagnosis")
    st.write("Questionnaire coming soon")

with tab3:
    st.header("Soil Report Analysis")
    st.write("Upload feature coming soon")