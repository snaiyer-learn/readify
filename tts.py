from gtts import gTTS
import nltk
import string
import os

with open("raw_sentences.txt", "r") as f:
    text = f.readlines()
cont = ""
for i in range(len(text)):
    temp = text[i].strip("\n") + " "
    temp = temp.replace(",", ".")
    cont += temp

sentences = nltk.sent_tokenize(cont)
print(sentences)
if os.path.exists("sentences.txt"):
    os.remove("sentences.txt")

with open('sentences.txt', 'w') as f:
    for line in sentences:
        f.write(f"{line}\n")


# engine = pyttsx3.init()

for i in range(len(sentences)):
    string = sentences[i]
    language='en'
    myobj=gTTS(text=string,lang=language,slow=True)
    myobj.save(r"""C:\Users\shariq\Desktop\Projects\readify\audio\\""" + str(i) +".mp3")
    # newVoiceRate = 80
    # engine.setProperty('rate',newVoiceRate)
    # engine.save_to_file(string, r"""C:\Users\shariq\Desktop\Projects\readify\audio\\""" + str(i) +".mp3")
    # engine.runAndWait()

