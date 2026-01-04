import streamlit as st
import numpy as np
import random
from PIL import Image

# -------------------------
# Page configuration
# -------------------------
st.set_page_config(
    page_title="Emotion Based Music Player",
    layout="centered"
)

st.title("🎵 Emotion-Based Music Player")
st.write("Capture an image to get an emotion-based YouTube song recommendation")

# -------------------------
# Load emotion labels
# -------------------------
labels = np.load("labels.npy", allow_pickle=True)

# -------------------------
# Emotion → YouTube embed mapping
# -------------------------
def get_youtube_embed(emotion: str):
    emotion = emotion.lower().strip()
    embeds = {
        "sad": "https://www.youtube.com/embed/pvppSBtG68c",
        "happy": "https://www.youtube.com/embed/pIvf9bOPXIw",
        "angry": "https://www.youtube.com/embed/d9r_c0Tg_q4",
        "neutral": "https://www.youtube.com/embed/pIvf9bOPXIw",
        "surprise": "https://www.youtube.com/embed/csx88cqa3y4",
    }
    return embeds.get(emotion)

# -------------------------
# Camera input (cloud-safe)
# -------------------------
img = st.camera_input("📷 Capture your face")

if img is not None:
    image = Image.open(img)
    st.image(image, caption="Captured Image", use_column_width=True)

    # ---------------------------------
    # Cloud-safe emotion selection
    # (replace with real model locally)
    # ---------------------------------
    emotion = random.choice(labels)
    emotion = str(emotion).lower().strip()

    st.success(f"Detected Emotion: {emotion.upper()}")

    # -------------------------
    # Song section (ALWAYS show)
    # -------------------------
    st.subheader("🎶 Recommended Song")

    embed_url = get_youtube_embed(emotion)

    if embed_url:
        st.components.v1.iframe(
            embed_url,
            height=420,
            scrolling=True
        )
    else:
        st.warning("No YouTube song mapped for this emotion.")
