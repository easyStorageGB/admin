import streamlit as st
import datetime

st.set_page_config(page_title="easyStorage: Low-cost storage near you!",  page_icon="🚚",)
st.image('eslogo.png', use_column_width=True)
st.write("# 🚚 Admin 🚀")

st.code(datetime.datetime.now().date())