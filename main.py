import os
import random
from gtts import gTTS
from moviepy.editor import *

# موضوعات آموزشی
topics = [
    "یک ترفند مخفی آیفون",
    "یک قابلیت جالب واتساپ",
    "یک روش افزایش تمرکز",
    "یک ترفند کاربردی گوشی"
]

topic = random.choice(topics)

script = f"امروز یاد میگیریم {topic}. برای آموزش‌های بیشتر کانال رو سابسکرایب کن!"

# ساخت صدا
tts = gTTS(script, lang='fa')
tts.save("voice.mp3")

# ساخت ویدیو عمودی 1080x1920
background = ColorClip(size=(1080,1920), color=(15,15,15), duration=15)

audio = AudioFileClip("voice.mp3")
video = background.set_audio(audio)

# خروجی با کیفیت بالا و 40fps
video.write_videofile(
    "short.mp4",
    fps=40,
    codec="libx264",
    audio_codec="aac",
    bitrate="8000k"
)

print("Video created successfully!")
