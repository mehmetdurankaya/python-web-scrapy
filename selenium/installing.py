from selenium import webdriver
import time

driver = webdriver.Chrome()
#driver= webdriver.Firefox()
url= "https://www.github.com"
driver.get(url)
time.sleep(2)
driver.maximize_window()
#driver.save_screenshot("github.com-homepage.png")

url= "https://www.github.com/mehmetdurankaya"
driver.get(url)
print(driver.title)
if "mehmetdurankaya" in driver.title:
    driver.save_screenshot("github-mehmetdurankaya.png")
time.sleep(2)
driver.back()
#driver.forward()
time.sleep(2)
driver.close()
