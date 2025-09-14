import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center;'>Welcome to Diet Recommendation System! 👋</h1>",
    unsafe_allow_html=True
)

st.sidebar.success("Select a recommendation app.")
st.markdown(
    """
    <h4 style='text-align: center;'>
    💻 ML Magic | 🔍 NearestNeighbors Vibes | ⚖️ BMI Tracker | 🍎 Calorie Crunch | 🥗 Smart Diet Picks | ⚡ FastAPI Backend | 🎨 Streamlit Frontend
    </h4>
    """,
    unsafe_allow_html=True
)