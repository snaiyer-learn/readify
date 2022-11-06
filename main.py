import subprocess
import os

subprocess.call("python tts.py", shell = True)
subprocess.call("python get_images.py", shell = True)
subprocess.call("python refineimages.py", shell = True)
subprocess.call("python use_morph.py", shell = True)
subprocess.call("python last.py", shell = True)
os.system('start vlc C:\\Users\\shariq\\Desktop\Projects\\readify\\result\output.mp4')
