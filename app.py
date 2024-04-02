import streamlit as st
from backend.new_chain import get_chain

chain = None

if chain == None:
    chain = get_chain()

st.title("Custom chatbot")

question = st.text_area("Enter your question here: ")

if st.button("Submit"):
    response = chain.invoke(question)
    
    st.write(response['result'])

