import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=60 * 60)  # Cache 100 entries for 1 hour
# Replace with your chosen LLM model name (if different from Llama-2)
llm_model_name = "model/llama-2-7b-chat.ggmlv3.q8_0.bin"
template= """Answer the below question
Question: {question}
"""

llm = CTransformers(model=llm_model_name, model_type='llama', config={'max_new_tokens': 256,'temperature':0.001})

def get_llm_response(user_question):
    prompt = PromptTemplate(
        input_variables=["question"],
        template = template)
    response = llm(prompt.format(question=user_question))
    return response
   
st.set_page_config(page_title="MuseAI", page_icon="🐪")
st.title(":blue[Hi👋🏻, I'm LlamaGenera a chatbot powered by an LLM to answer your questions.]")
st.header(":violet[How may I help you?] 😄")

st.empty()

def update_chat_display(user_question,response):
    st.write("👧🏽: " +user_question)
    if response:
        st.markdown("🤖: " +response)
    else:
        st.markdown("🤖: " + " :red[Sorry :( I do not have the required data to answer your question]")

user_question = st.chat_input(placeholder="Enter your question...")

if user_question:
    response = get_llm_response(user_question)
    update_chat_display(user_question,response)