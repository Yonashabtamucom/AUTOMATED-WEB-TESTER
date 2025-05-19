 Automated Web Tester

A simple yet powerful automated web testingtool built using Python and Selenium.  
It opens a browser, visits a website (e.g., Wikipedia), performs a search, and captures screenshots — all automatically.
---
Features

- Search Automation: Automates search on websites like Wikipedia  
- Browser Control: Launch and control Chrome browser with Selenium  
- Smart Waiting: Waits for elements to load before interacting  
- Screenshot Capture: Save snapshots of the result page  
- Clean Exit: Closes browser after execution

---
How It Works

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Selenium (software)")
search_box.send_keys(Keys.RETURN)

time.sleep(10)
driver.save_screenshot("wikipedia_result.png")
driver.quit()
```

---
Project Structure

```
Automated-Web-Tester
├── CORRECTAUTOMATEDWEBTESTER CODE.py
├── wikipedia1.png
├── wikipedia2.png
├── wikipedia3.png
├── README.md
└── LICENSE
```

---

Screenshots

| Wikipedia Search | Result Page |
|------------------|-------------|
| ![](./wikipedia1.png) | ![](./wikipedia2.png) |
| ![](./wikipedia3.png) |             |

---

 Requirements

- Python 3.x  
- Selenium  
- Chrome + ChromeDriver

Install dependencies:

pip install selenium
 License

This project is licensed under the [MIT License](LICENSE)

---
 Author

Made with ❤️ by [Yonashabtamucom](https://github.com/Yonashabtamucom)
