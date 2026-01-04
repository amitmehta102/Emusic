import streamlit as st
import numpy as np
import random
from PIL import Image
from music import get_music

st.set_page_config(page_title="Emotion Based Music Player")

st.title("🎵 Emotion-Based Music Player")
st.write("Capture an image to get emotion-based music")

labels = np.load("labels.npy", allow_pickle=True)

img = st.camera_input("Capture your face")

if img is not None:
    image = Image.open(img)
    st.image(image, caption="Captured Image")

    # Cloud-safe emotion selection
    emotion = random.choice(labels)
    st.success(f"Detected Emotion: {emotion}")

    music_url = get_music(emotion)
    if music_url:
        st.audio(music_url)
