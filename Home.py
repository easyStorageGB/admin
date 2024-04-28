import streamlit as st, pathlib, os, openai, tiktoken
import utilities as ut

st.set_page_config(page_title="easyStorage: Low-cost storage near you!",  page_icon="🚚",)
st.image('eslogo.png', use_column_width=True)
st.write("# 🚚 Admin 🚀")

