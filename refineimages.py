from PIL import Image
import os

dir_path = os.path.dirname(os.path.realpath(__file__))+ "/images/"

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

# print result
print(res)

for i in res:
    im = Image.open('images/'+i)
    cropped = im.crop((60,208,1020,1778))
    cropped.save('images/'+i)


