import streamlit as st
from langchain.callbacks import get_openai_callback
from qa_model import ask, select_model, build_qa_model


def page_ask_my_vtt():
    st.markdown("#### クエリ 例")

    st.caption("文字起こしに質問が出来ます")
    st.markdown(" - 何について話をしていますか")
    st.markdown(" - 誤字脱字は前後の文脈から推測して修正し、トピック毎で会話をまとめて、箇条書きにしてください")
    st.markdown("---")

    llm = select_model()
    container = st.container()
    response_container = st.container()

    with container:
        query = st.text_input("Query: ", key="input")
        if not query:
            answer = None
        else:
            qa = build_qa_model(llm)
            if qa:
                with st.spinner("ChatGPT is typing ..."):
                    answer, cost = ask(qa, query)
            else:
                answer = None

        if answer:
            with response_container:
                st.markdown("## Answer")
                st.write(answer)
