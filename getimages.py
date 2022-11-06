from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import os

chrome_options = Options() 
# chrome_options.add_experimental_option("detach", True)
prefs = {"download.default_directory" : r"C:\Users\shariq\Desktop\Projects\readify\images\\","directory_upgrade": True}
chrome_options.add_experimental_option("prefs",prefs)

with open("sentences.txt", "r") as f:
    text = f.readlines()

for i in range(len(text)):
    text[i] = text[i].strip("\n")

for k in text:
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.wombo.art/create")

    time.sleep(5)

    inputElement = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/input""")
    inputElement.send_keys(k)

    button = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[3]/div/div/img""")
    button.click()

    button2 = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[1]/div[2]/button""")
    button2.click()

    time.sleep(15)

    button3 = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[2]/div/div[2]/button""")
    button3.click()

    time.sleep(5)
    print("Image saved")

driver.close()

dir_path = os.path.dirname(os.path.realpath(__file__))+ "/images/"
res = []
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

for i in res:
    im = Image.open('images/'+i)
    cropped = im.crop((60,208,1020,1778))
    cropped.save('images/'+i)