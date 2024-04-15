import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Replace with your chosen LLM model name (if different from Llama-2)
llm_model_name = "model/llama-2-7b-chat.ggmlv3.q8_0.bin"

template= """Could you answer the below question
Question: {question}
"""

def get_llm_response(user_question):
    prompt = PromptTemplate(
        input_variables=["question"],
        template = template)
    # Use CTransformers or your chosen library here
    llm = CTransformers(model=llm_model_name, model_type="llama", config={"temperature": 0})
    print(llm)
    response = llm(prompt.format(question=user_question))
    return response
   

st.set_page_config(page_title="MuseAI", page_icon="🐪")
st.title("Hi👋🏻, I'm MuseAI a chatbot powered by an LLM to answer your questions in real time.")
st.header("How may I help you?")


def update_chat_display(user_question,response):
    st.write("👧🏽: "+user_question)
    st.markdown("🤖: " +response)


user_question = st.chat_input(placeholder="Enter your question...")

if user_question:
    response = get_llm_response(user_question)
    update_chat_display(user_question,response)
    
    

   

