import streamlit as st
import datetime, hmac

st.set_page_config(page_title="easyStorage: Low-cost storage near you!",  page_icon="🚚",)
st.image('eslogo.png')
st.write("# Admin ")

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["PASSWORD"], st.secrets["PASSWORD"]):
            st.session_state["password_correct"] = True
            del st.session_state["PASSWORD"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Enter passkey: ", type="password", on_change=password_entered, key="PASSWORD"
    )
    
    if "password_correct" in st.session_state:
        st.error("😕 Passkey incorrect, try again")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
st.success("Hello Admin, the passkey is correct! ")
