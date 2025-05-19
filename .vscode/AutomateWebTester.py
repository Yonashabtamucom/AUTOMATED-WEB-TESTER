from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options=Options()
chrome_options.add_argument("--start-maximized")
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://www.wikipedia.org")
search_box=driver.find_element(By.NAME,"search")
search_box.send_keys("I like python")
search_box.send_keys(Keys.RETURN)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h3")))
first_result=driver.find_element(By.CSS_SELECTOR,'h3')
first_result.click()
time.sleep(10)
driver.save_screenshot("openai_result.png")
print('Screenshot saved as openai result.png')
driver.quit()