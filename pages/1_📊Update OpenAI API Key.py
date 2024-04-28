import streamlit as st
from utils import st_def
from cryptography.fernet import Fernet
import pymongo
import base64


st.image('eslogo.png', use_column_width=True)
st.write("# 🚚 Admin 🚀")

password = st.text_input("Copy/Paste the OpenAI API Key, and press Enter", type="password")

if password:
    st.code("You entered: " + password[:22] + "...")
    # Your key
    # key_bytes = Fernet.generate_key()

    # # Convert bytes key to base64 encoded string
    # key_string = base64.urlsafe_b64encode(key_bytes).decode()

    # # Save the key to a file
    # with open('key.txt', 'w') as keyfile:
    #     keyfile.write(key_string)

    uri = st.secrets["MONGO_URI"]

    @st.cache_resource
    def init_connection():
        return pymongo.MongoClient(uri)

    client = init_connection()

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        mydatabase = client.easystorage
        mycollection = mydatabase.openai
        print(mycollection)
    except Exception as e:
        print(e)

    # Pull data from the collection.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def get_data():
        items = mycollection.find()
        items = list(items)  # make hashable for st.cache_data
        return items

    items = get_data()

    st_key = st.secrets["FERNET"]
    key_bytes = base64.urlsafe_b64decode(st_key)
    cipher_suite = Fernet(key_bytes)
    value = cipher_suite.encrypt(password.encode())
    filter_query = {"0.name": "key"}
    update_query = {"$set": {"0.value": value}}

    # Update the document
    result = mydatabase.openai.update_one(filter_query, update_query)

    # Check if the update was successful
    if result.modified_count > 0:
        print("Update successful!")
    else:
        print("No documents matched the filter.")
        
    query = {"0.name": "key"}

    # Execute the query
    result = mycollection.find_one(query)

    # Check if the document was found
    if result:
        # Extract the value
        value = result['0']['value']
        st.info("The OpenAI API Key is successfully embedded and saved!")
    else:
        print("Document not found.")