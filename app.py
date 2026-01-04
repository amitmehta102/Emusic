import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import cv2

st.set_page_config(page_title="Emotion Based Music Player")

st.title("🎵 Emotion-Based Music Player")
st.write("Capture an image to detect emotion")

# Load model and labels
model = load_model("model.h5")
labels = np.load("labels.npy", allow_pickle=True)

img = st.camera_input("Take a picture")

def preprocess(image):
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (48, 48))
    image = image / 255.0
    image = image.reshape(1, 48, 48, 1)
    return image

if img is not None:
    image = Image.open(img)
    st.image(image, caption="Captured Image")

    processed = preprocess(image)
    pred = model.predict(processed)
    emotion = labels[np.argmax(pred)]

    st.success(f"Detected Emotion: {emotion}")
