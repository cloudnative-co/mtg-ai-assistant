import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_vtt_text(combined_vtt):
    with st.spinner("[STEP 4/5] 文字起こしをベクトル化しています..."):
        if combined_vtt is not None:
            text = combined_vtt
            text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                    model_name="text-embedding-ada-002",
                    chunk_size=500,
                    chunk_overlap=0,
                    )
            return text_splitter.split_text(text)
