from selenium import webdriver
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Your User Agent Here")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = "https://www.amazon.in/s?k=laptop&crid=3UDEHJVP3RJV6&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent"
driver.get(url)

titles =  driver.find_element(By.CLASS_NAME,"a-size-medium.a-color-base.a-text-normal").text
prices = driver.find_element(By.CLASS_NAME,"a-price").text
offer = driver.find_element(By.CLASS_NAME,"a-section.a-spacing-none.a-spacing-top-micro.puis-price-instructions-style").text
links = driver.find_element(By.CLASS_NAME,"a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
linkss  = links.get_attribute('href')


print("titles",titles)
print("prices",prices)
print("offer",offer[23:35])
print("link",linkss)
driver.get(linkss)
offers = driver.find_element(By.CLASS_NAME,"a-carousel")
print("offers",offers.text)

detailedOffers = links.find_element(By.CLASS_NAME,"a.spacing-mini.a-size-base-plus")
print("detailedOffers",detailedOffers.text)