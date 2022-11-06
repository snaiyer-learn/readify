# import pip

# def install(package):
#     pip.main(['install', package])

# # Example
# if __name__ == '__main__':
#     install('pyttsx3')
import pyttsx3
engine = pyttsx3.init()
string = "Humpty dumpty sat on a wall"
engine.save_to_file(string, 'speech.mp3')
engine.runAndWait()
# save this file as tts.mp3
