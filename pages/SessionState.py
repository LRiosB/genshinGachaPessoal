import streamlit as st

st.set_page_config(
    page_title="SessionStateAdmin",
    page_icon="👋",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



st.write(st.session_state)