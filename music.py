def get_music(emotion):
    music_map = {
        "happy": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "sad": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "angry": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "neutral": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
        "surprise": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
    }
    return music_map.get(emotion)
