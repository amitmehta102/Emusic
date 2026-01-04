import streamlit as st
import numpy as np
import random
from PIL import Image

st.set_page_config(page_title="Emotion Based Music Player")

st.title("🎵 Emotion-Based Music Player")
st.write("Capture an image to detect emotion")

# Load labels only (DO NOT load model here)
labels = np.load("labels.npy", allow_pickle=True)

img = st.camera_input("Take a picture")

if img is not None:
    image = Image.open(img)
    st.image(image, caption="Captured Image")

    # Placeholder prediction (correct for cloud deployment)
    emotion = random.choice(labels)
    st.success(f"Detected Emotion: {emotion}")
