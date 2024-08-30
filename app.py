from selenium import webdriver
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Your User Agent Here")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = "https://www.amazon.in/s?k=laptop&crid=3UDEHJVP3RJV6&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent"
driver.get(url)
print(url)