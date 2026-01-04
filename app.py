import streamlit as st
import numpy as np
import random
from PIL import Image
from music import get_youtube_embed

st.set_page_config(page_title="Emotion Based Music Player")

st.title("🎵 Emotion-Based Music Player")
st.write("Emotion-based YouTube playlist recommendation")

labels = np.load("labels.npy", allow_pickle=True)

img = st.camera_input("Capture your face")

if img is not None:
    image = Image.open(img)
    st.image(image, caption="Captured Image")

    # Cloud-safe emotion selection (or use your detected emotion)
    emotion = random.choice(labels)
    st.success(f"Detected Emotion: {emotion.upper()}")

    embed_url = get_youtube_embed(emotion)
    if embed_url:
        st.subheader("▶️ Recommended YouTube Playlist")
        st.components.v1.iframe(
            embed_url,
            height=420,
            scrolling=True
        )
