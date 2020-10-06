#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from googletrans import Translator
f = open('C:\\Users\\Monica\\Desktop\\Projects\\Python Projects 1\\SpeechRecognition\\largefiles_Conversion\\recognized.txt','r')
if f.mode=='r':
    contents = f.read()
    print(contents)
    t = Translator().translate(contents,dest='nl')
    print(t.text)
    
with open('recognized_2.txt','w', encoding = "utf-8") as f:
    f.write(t.text)

