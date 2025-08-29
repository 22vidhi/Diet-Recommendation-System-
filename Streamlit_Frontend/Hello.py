import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation System! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A web app that provides personalized diet suggestions using content-based filtering. Built with Scikit-Learn, FastAPI, and Streamlit.
    """
)
