import os
import subprocess

aud = []
dir_path = os.path.dirname(os.path.realpath(__file__))+ "/images/"

for path in os.listdir(dir_path):
    x = path.replace(" ", "")
    os.rename("images/"+path,"images/"+x)

res = ['Dream_TradingCard.jpg']
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        if path != 'Dream_TradingCard.jpg':
            res.append(path)


for i in range(len(res)-1):
    subprocess.call("python morph.py -s" + "images/"+res[i] + " -t " + "images/"+res[i+1] +" --steps 350 ", shell = True)

