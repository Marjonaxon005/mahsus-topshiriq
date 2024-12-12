# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lxgdL1TM8kdMmNcZbY4-U_TAf4aznSj5
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("malibu.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("soat.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("images.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

import numpy as np
import matplotlib.pyplot as plt

# Sinus funksiyasining x qiymatlarini belgilaymiz
x = np.linspace(0, 10, 100)  # 0 dan 10 gacha bo'lgan 100 ta nuqta
y = np.sin(x)  # sinus funksiyasining qiymatlari

# Grafikni chizamiz
plt.figure(figsize=(8, 5))  # grafik o'lchami
plt.plot(x, y, label="Sinus(x)", color="blue")  # sinus grafigi
plt.title("Sinus Funksiyasining Grafikasi")  # sarlavha
plt.xlabel("X qiymatlari")  # x o'qi nomi
plt.ylabel("Y qiymatlari")  # y o'qi nomi
plt.grid(True)  # tarmoq chizmalari
plt.legend()  # legendani ko'rsatish
plt.show()  # grafikni ko'rsatish

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,21,9, 2,5, 8,  9, 7,5,7,9,8,2, 6, ])
y = np.array([1,9,13,21,9, 2,5, 8, 9, 6, 8 ,4, 9,2,6,3,9])
plt.scatter(x,y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'piano.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "Hi everyone how are you My name is Marjona"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)

# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)

import pandas as pd

file_path = 'WHO COVID-19 cases.csv'
df = pd.read_csv(file_path)


sorted_df = df.sort_values(by='Country')

filtr=df[(df['Country_code']=="AF")]
print(filtr)

import pandas as pd

file_path = 'WHO COVID-19 cases.csv'
df = pd.read_csv(file_path)


sorted_df = df.sort_values(by='Country')

filtr=df[(df['Country_code']=="AD")]
print(filtr)

import pandas as pd

file_path = 'WHO COVID-19 cases.csv'
df = pd.read_csv(file_path)


sorted_df = df.sort_values(by='Country')

filtr=df[(df['Country_code']=="AZ")]
print(filtr)