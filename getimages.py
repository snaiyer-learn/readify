from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.wombo.art/create")

inputElement = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/input""")
inputElement.send_keys('Humpty dumpty sat on a wall')

button = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[3]/div/div/img""")
button.click()

button2 = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[1]/div[2]/button""")
button2.click()

time.sleep(15)

button3 = driver.find_element(By.XPATH, """//*[@id="blur-overlay"]/div/div/div[2]/div/div[2]/button""")
button3.click()
