import streamlit as st
import pymongo

st.set_page_config(page_title="easyStorage: Low-cost storage near you!",  page_icon="🚚",)
st.image('eslogo.png')

if not st.session_state.get("password_correct", False):
    st.error("Please enter passkey at Home Page to continue.")
else:
    st.write("## 🦜Update Prompt")
    with st.spinner("Loading..."):
        uri = st.secrets["MONGO_URI"]
        @st.cache_resource
        def init_connection():
            return pymongo.MongoClient(uri)
        client = init_connection()
        content = "Default"
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            mydb = client.easystorage
            myco = mydb.esprompt
            query = {"item" : "prompt"}
            result = myco.find_one(query)
            if result:
                content = result.get("content", None)
        except Exception as e:
            print(e)

        prompt = st.text_area("Modify the Prompt and press Enter", content, height=200)

        confirmation = st.checkbox("Check to confirm")

        # Button to send the text
        if confirmation and st.button("Click to update the Prompt"):

            filter_query = {"item" : "prompt"}
            update_query = {"$set": {"content": prompt}}

            # Update the document
            result = myco.update_one(filter_query, update_query)

            # Check if the update was successful
            if result.modified_count > 0:
                st.success("The prompt is successfully updated!")
            else:
                print("Something wrong. Try again later.")
