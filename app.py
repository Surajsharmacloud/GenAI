import os
import streamlit as st
from langchain_community.llms import ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#streamlit FrameWork
st.title("LangChain Demo With Ollama Gemma:2b")

input_text=st.text_input("What question you have in mind?")

#Ollama gemma:2b
llm=ChatOllama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    

