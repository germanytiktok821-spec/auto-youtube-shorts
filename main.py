import random
import os
from gtts import gTTS

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

# ساخت ویدیو با ffmpeg (پس‌زمینه مشکی 1080x1920 با 40fps)
os.system(
    "ffmpeg -f lavfi -i color=c=black:s=1080x1920:d=15 "
    "-i 
