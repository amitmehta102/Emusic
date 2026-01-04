def get_music(emotion):
    """
    Returns a message based on emotion.
    (Music files can be added later if needed)
    """
    emotion_map = {
        "happy": "Playing happy mood music 🎶",
        "sad": "Playing calm sad music 🎵",
        "angry": "Playing relaxing music 🎧",
        "neutral": "Playing neutral mood music 🎼",
        "surprise": "Playing energetic music 🎺"
    }

    return emotion_map.get(emotion, "Playing default music 🎶")
