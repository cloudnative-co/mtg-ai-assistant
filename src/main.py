from config import *
from utils import init_page, get_audio
from audio_processing import split_audio, adjust_timestamp
from transcription import transcribe_chunk, generate_vtt, combine_vtt_files
from qdrant_utils import load_qdrant, recreate_qdrant, build_vector_store
from text_processing import get_vtt_text
from vector_db_page import page_vtt_upload_and_build_vector_db
from query_page import page_ask_my_vtt
from qa_model import select_model, build_qa_model, ask
import streamlit as st
import streamlit_scrollable_textbox as stx


def main():
    init_page()

    audio_file = None
    combined_vtt = None

    with st.empty():
        st.write("動画 or 音声データをアップロードしてください。")
        if audio_file is None:
            audio_file = get_audio()

        # m4aかmp3で有ればst.audioで、mp4で有ればst.videoで再生
        if audio_file is not None and audio_file.name.lower().endswith('.mp4'):
            st.video(audio_file, format='video/mp4')
        elif audio_file is not None and audio_file.name.lower().endswith('.m4a'):
            st.audio(audio_file, format='audio/m4a')
        elif audio_file is not None and audio_file.name.lower().endswith('.mp3'):
            st.audio(audio_file, format='audio/mp3')

    selection = st.sidebar.radio("Menu", ["speech to text", "query"])

    if selection == "speech to text":
        with st.empty():
            if st.session_state.combined_vtt is not None:
                stx.scrollableTextbox(st.session_state.combined_vtt, height=600)

            elif st.session_state.combined_vtt is None:
                if audio_file is not None:
                    counter = split_audio(audio_file)
                    generate_vtt(counter)

                    if st.session_state.combined_vtt is None:
                        combined_vtt = combine_vtt_files(counter)
                        st.session_state.combined_vtt = combined_vtt
                        page_vtt_upload_and_build_vector_db(st.session_state.combined_vtt)
                        stx.scrollableTextbox(combined_vtt, height=600)
                    elif st.session_state.combined_vtt is not None:
                        stx.scrollableTextbox(st.session_state.combined_vtt, height=600)

    elif selection == "query":
        if st.session_state.combined_vtt is not None:
            page_ask_my_vtt()


if __name__ == "__main__":
    main()
