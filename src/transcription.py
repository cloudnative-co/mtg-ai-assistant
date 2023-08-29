import openai
import re
import os
from concurrent.futures import ThreadPoolExecutor
from audio_processing import adjust_timestamp
import streamlit as st
from config import OUTPUT_DIR, SPLIT_SECONDS


def transcribe_chunk(filename):
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe(model="whisper-1",
                                             file=audio_file,
                                             response_format="vtt",
                                             language="ja",
                                             )
    return transcript


def generate_vtt(counter):
    with st.spinner("[STEP 2/5] 文字起こしを生成しています..."):
        with ThreadPoolExecutor() as executor:
            filenames = [os.path.join(OUTPUT_DIR, f'chunk{i}.mp3') for i in range(counter)]
            transcripts = executor.map(transcribe_chunk, filenames)
            for i, transcript in enumerate(transcripts):
                adjusted_transcript = adjust_timestamp(transcript, i * SPLIT_SECONDS)
                with open(os.path.join(OUTPUT_DIR, f'chunk{i}.vtt'), 'w') as f:
                    f.write(adjusted_transcript)
                st.code(transcript, language='vtt')


def combine_vtt_files(counter):
    with st.spinner("[STEP 3/5] 文字起こしを結合しています..."):
        combined_vtt = "WEBVTT\n\n"
        for i in range(counter):
            with open(os.path.join(OUTPUT_DIR, f'chunk{i}.vtt'), 'r') as f:
                vtt_content = f.read()
                combined_vtt += vtt_content
        with open(os.path.join(OUTPUT_DIR, 'combined.vtt'), 'w') as f:
            f.write(combined_vtt)
        return combined_vtt
