import random

emotion_music = {
    "happy": ["music/happy1.mp3"],
    "sad": ["music/sad1.mp3"],
    "angry": ["music/angry1.mp3"],
    "neutral": ["music/neutral1.mp3"],
    "surprise": ["music/surprise1.mp3"]
}

def get_music(emotion):
    if emotion in emotion_music:
        return random.choice(emotion_music[emotion])
    return None
