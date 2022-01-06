import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="vi")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()

if "hello" in text:
    speak("Sửa đổi, bổ sung một số điều của Nghị định số 27/2019/NĐ-CP ngày 13 tháng 3 năm 2019 của Chính phủ quy định chi tiết một số điều của Luật Đo đạc và bản đồ (31/12/2021)")
elif "what is your name" in text:
    speak("My name is Hieu")
