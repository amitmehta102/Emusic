import streamlit as st
import numpy as np
import random
from PIL import Image

st.set_page_config(page_title="Emotion Based Music Player")

st.title("🎵 Emotion-Based Music Player")
st.write("Cloud demo version (UI workflow)")

labels = np.load("labels.npy", allow_pickle=True)

img = st.camera_input("Capture your face")

if img is not None:
    image = Image.open(img)
    st.image(image, caption="Captured Image")

    # Placeholder prediction (cloud-safe)
    emotion = random.choice(labels)
    st.success(f"Detected Emotion: {emotion}")
    st.info("🎶 Music recommended based on emotion")
