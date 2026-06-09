from gtts import gTTS
from moviepy.editor import *
import random

# موضوعات آموزشی
topics = [
    "یک ترفند مخفی آیفون",
    "یک قابلیت جالب واتساپ",
    "یک روش افزایش تمرکز",
    "یک ترفند کاربردی کیبورد آیفون"
]

topic = random.choice(topics)

script = f"امروز یاد میگیریم {topic}. برای آموزش‌های بیشتر کانال رو سابسکرایب کن!"

# ساخت صدا
tts = gTTS(script, lang='fa')
tts.save("voice.mp3")

# ساخت ویدیو عمودی
background = ColorClip(size=(1080,1920), color=(0,0,0), duration=15)
audio = AudioFileClip("voice.mp3")
video = background.set_audio(audio)

video.write_videofile("short.mp4", fps=24)
