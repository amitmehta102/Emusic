def get_music(emotion):
    music_map = {
        "happy": "music/happy.mp3",
        "sad": "music/sad.mp3",
        "angry": "music/angry.mp3",
        "neutral": "music/neutral.mp3",
        "surprise": "music/surprise.mp3"
    }
    return music_map.get(emotion, None)
