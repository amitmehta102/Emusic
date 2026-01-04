def get_youtube_embed(emotion):
    embeds = {
        "sad": "https://www.youtube.com/embed/pvppSBtG68c",
        "happy": "https://www.youtube.com/embed/pIvf9bOPXIw",
        "angry": "https://www.youtube.com/embed/d9r_c0Tg_q4",
        "neutral": "https://www.youtube.com/embed/pIvf9bOPXIw",
        "surprise": "https://www.youtube.com/embed/csx88cqa3y4",
    }
    return embeds.get(emotion)
