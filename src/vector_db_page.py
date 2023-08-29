import streamlit as st
from text_processing import get_vtt_text
from qdrant_utils import build_vector_store


def page_vtt_upload_and_build_vector_db(combined_vtt):
    container = st.container()
    with container:
        vtt_text = get_vtt_text(combined_vtt)
        if vtt_text:
            with st.spinner("[STEP 5/5] 文字起こしをベクトルDBに格納しています ..."):
                build_vector_store(vtt_text)
