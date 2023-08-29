from pydub import AudioSegment
import os
import re
import streamlit as st
from config import SPLIT_SECONDS, OUTPUT_DIR


def split_audio(audio_file):
    audio = AudioSegment.from_file(audio_file)
    length_audio = len(audio)
    start = 0
    threshold = SPLIT_SECONDS * 1000
    counter = 0

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for file_name in os.listdir(OUTPUT_DIR):
        os.unlink(os.path.join(OUTPUT_DIR, file_name))

    with st.spinner("[STEP 1/5] 音声ファイルを解析しています..."):
        while start < length_audio:
            end = min(length_audio, start + threshold)
            chunk = audio[start:end]
            filename = os.path.join(OUTPUT_DIR, f'chunk{counter}.mp3')
            chunk.export(filename, format="mp3")
            counter += 1
            start += threshold

    return counter


def adjust_timestamp(transcript, offset_seconds):
    transcript = transcript.replace('WEBVTT\n\n', '')

    def replacer(m):
        hours, minutes, seconds, milliseconds = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        total_seconds = hours * 3600 + minutes * 60 + seconds + offset_seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

    transcript = re.sub(r'(\d{2}):(\d{2}):(\d{2}).(\d{3})', replacer, transcript)

    return transcript
