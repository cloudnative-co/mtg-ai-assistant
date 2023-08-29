from config import APP_NAME
import streamlit as st


def init_page():
    st.set_page_config(
        page_title=APP_NAME,
    )
    st.title(APP_NAME)

    with open("images/logo.svg", "r") as f:
        svg = f.read()

    with st.sidebar:
        st.markdown(svg, unsafe_allow_html=True)
        st.markdown('---')

    if 'combined_vtt' not in st.session_state:
        st.session_state.combined_vtt = None


def get_audio():
    audio_file = st.file_uploader("Zoomの音声か動画をアップロードしてください",
                                  type=['mp3', 'm4a', 'mp4'])
    return audio_file
