#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gtts import gTTS
import os

file = open("recognized_2.txt","r").read().replace("\n"," ")
speech = gTTS(text = str(file), lang = 'nl', slow = False)
speech.save("audio_2.mp3")
os.system("audio_2.mp3")

