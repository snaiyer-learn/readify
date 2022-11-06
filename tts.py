# import pip

# def install(package):
#     pip.main(['install', package])

# # Example
# if __name__ == '__main__':
#     install('pyttsx3')
import pyttsx3
engine = pyttsx3.init()
string = "Humpty dumpty sat on a wall"
newVoiceRate = 100
engine.setProperty('rate',newVoiceRate)
engine.save_to_file(string, 'audio/speech.mp3')
engine.runAndWait()

