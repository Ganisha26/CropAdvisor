import streamlit as st

st.set_page_config(page_title="Crop Advisor")

st.title("🌱 Crop Advisor")

tab1, tab2, tab3 = st.tabs([
    "Quick Ask",
    "Guided Diagnosis",
    "Soil Report Analysis"
])
from sentence_transformers import SentenceTransformer
import chromadb

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def load_db():
    client = chromadb.PersistentClient(path="vector_db")
    return client.get_collection("agri_knowledge")

model = load_model()
collection = load_db()

with tab1:
    st.header("Quick Ask")

    question = st.text_input("Ask an agricultural question")
    search=st.button("Search")

    if search and question:
        query_embedding = model.encode(question).tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=1
        )

        st.subheader("Answer")
        st.write(results["documents"][0][0])
with tab2:
    st.header("Guided Diagnosis")

    crop = st.selectbox(
        "Which crop do you want to grow?",
        ["Rice", "Wheat", "Cotton", "Soybean", "Maize"]
    )

    soil = st.selectbox(
        "What is your soil type?",
        ["Black", "Red", "Sandy", "Loamy", "Don't Know"]
    )

    irrigation = st.radio(
        "Do you have irrigation?",
        ["Yes", "No"]
    )

    if st.button("Generate Recommendation"):
        st.success("Assessment Generated")
        st.write("Crop:", crop)
        st.write("Soil:", soil)
        st.write("Irrigation:", irrigation)
with tab3:
    st.header("Soil Report Analysis")
    st.write("Upload feature coming soon")