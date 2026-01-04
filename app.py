import streamlit as st
import numpy as np
import cv2
import mediapipe as mp
from tensorflow.keras.models import load_model
from music import get_music

st.set_page_config(page_title="Emotion Based Music Player")

# Load model and labels
model = load_model("model.h5")
labels = np.load("labels.npy", allow_pickle=True)

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False)

st.title("🎵 Emotion-Based Music Player")
st.image("emotion.png", use_column_width=True)

run = st.checkbox("Start Camera")
frame_window = st.image([])

cap = cv2.VideoCapture(0)

def extract_landmarks(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        landmarks = []
        for lm in result.multi_face_landmarks[0].landmark:
            landmarks.extend([lm.x, lm.y])
        return np.array(landmarks).reshape(1, -1)
    return None

while run:
    ret, frame = cap.read()
    if not ret:
        st.error("Camera not accessible")
        break

    landmarks = extract_landmarks(frame)
    if landmarks is not None:
        prediction = model.predict(landmarks)
        emotion = labels[np.argmax(prediction)]

        st.success(f"Detected Emotion: {emotion}")
        st.info(get_music(emotion))

    frame_window.image(frame, channels="BGR")

cap.release()
