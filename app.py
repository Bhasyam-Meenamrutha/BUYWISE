from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

app = Flask(__name__)
def scrape_amazon(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Your User Agent Here")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    query_formatted = query.replace(" ", "+")
    url = f'https://www.amazon.in/s?k={query_formatted}'

    driver.get(url)

    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot")))
    except Exception as e:
        print(f"Error waiting for page load: {e}")
    
    time.sleep(random.uniform(2, 5))

    parent_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 's-main-slot')]//div[contains(@class, 's-result-item') and @data-component-type='s-search-result']")

    products = []
    for parent in parent_elements:
        try:
            heading = parent.find_element(By.CSS_SELECTOR, "h2 a span").text
            link = parent.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
            try:
                cost = parent.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            except:
                cost = "Price not available"
            try:
                offerparent = parent.find_element(By.CSS_SELECTOR, ".a-row.a-size-base.a-color-base")
                offer_text = offerparent.text
                start_index = offer_text.find("(")
                end_index = offer_text.find(")")
                if start_index != -1 and end_index != -1:
                    discount = offer_text[start_index:end_index + 1]
                else:
                    discount = "No discount found"
            except:
                discount = "No discount found"

            # New code to extract image URL
            try:
                image_element = parent.find_element(By.CSS_SELECTOR, "img.s-image")
                image_url = image_element.get_attribute("src") if image_element else "No Image"
            except Exception as e:
                image_url = "No Image"
                print(f"Error occurred while processing product image: {e}")

            products.append({
                "name": heading,
                "link": link,
                "cost": cost,
                "offer": discount,
                "image": image_url  # Add image URL to the product data
            })

        except Exception as e:
            print(f"Error extracting data: {e}")

    driver.quit()
    return products

def scrape_flipkart_chairs(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Your User Agent Here")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    query_formatted = query.replace(" ", "+")
    url = f'https://www.flipkart.com/search?q={query_formatted}'
    driver.get(url)

    data = []

    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "slAVV4")))

        products = driver.find_elements(By.CLASS_NAME, "slAVV4")

        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, ".wjcEIp").text if product.find_elements(By.CSS_SELECTOR, ".wjcEIp") else "No Title"
                price = product.find_element(By.CSS_SELECTOR, ".Nx9bqj").text if product.find_elements(By.CSS_SELECTOR, ".Nx9bqj") else "No Price"
                offer_percentage = product.find_element(By.CSS_SELECTOR, ".UkUFwK").text if product.find_elements(By.CSS_SELECTOR, ".UkUFwK") else "No Offer"
                link_element = product.find_element(By.CSS_SELECTOR, ".VJA3rP") if product.find_elements(By.CSS_SELECTOR, ".VJA3rP") else None
                link = link_element.get_attribute("href") if link_element else "No Link"
                image_element = product.find_element(By.CLASS_NAME, "DByuf4") if product.find_elements(By.CLASS_NAME, "DByuf4") else None
                image_url = image_element.get_attribute("src") if image_element else "No Image"
                
                data.append({
                    'name': title,
                    'link': link,
                    'cost': price,
                    'offer': offer_percentage,
                    'image':image_url
                })
            except Exception as e:
                print(f"Error occurred while processing product: {e}")
    except Exception as e:
        print(f"An error occurred while loading the page or finding products: {e}")
    
    driver.quit()
    return data

def scrape_flipkart_electronics(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Your User Agent Here")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    query_formatted = query.replace(" ", "+")
    url = f'https://www.flipkart.com/search?q={query_formatted}'
    driver.get(url)

    data = []

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_75nlfW")))

        products = driver.find_elements(By.CLASS_NAME, "_75nlfW")

        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, ".KzDlHZ").text if product.find_elements(By.CSS_SELECTOR, ".KzDlHZ") else "No Title"
                moreDetails = product.find_element(By.CLASS_NAME, "G4BRas").text
                price = product.find_element(By.CSS_SELECTOR, ".Nx9bqj._4b5DiR").text if product.find_elements(By.CSS_SELECTOR, ".Nx9bqj._4b5DiR") else "No Price"
                offer_percentage = product.find_element(By.CSS_SELECTOR, ".UkUFwK").text if product.find_elements(By.CSS_SELECTOR, ".UkUFwK") else "No Offer"
                link_element = product.find_element(By.CSS_SELECTOR, ".CGtC98") if product.find_elements(By.CSS_SELECTOR, ".CGtC98") else None
                link = link_element.get_attribute("href") if link_element else "No Link"
                image_element = product.find_element(By.CLASS_NAME, "DByuf4") if product.find_elements(By.CLASS_NAME, "DByuf4") else None
                image_url = image_element.get_attribute("src") if image_element else "No Image"
                
                data.append({
                    'name': title,
                    'link': link,
                    'cost': price,
                    'offer': offer_percentage,
                    'image':image_url
                })
            except Exception as e:
                print(f"Error occurred while processing product: {e}")

    except Exception as e:
        print(f"An error occurred while loading the page or finding products: {e}")

    driver.quit()
    return data

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/index', methods=['GET'])
def index():
    query = request.args.get('query')
    amazon_data = []
    flipkart_data = []
    
    if query:
        keywords = ["mobile", "phone", "laptop"]
        if any(keyword in query.lower() for keyword in keywords):
            amazon_data = scrape_amazon(query)
            flipkart_data = scrape_flipkart_electronics(query)
        else:
            amazon_data = scrape_amazon(query)
            flipkart_data = scrape_flipkart_chairs(query)
        
    return render_template('index.html', amazon_data=amazon_data, flipkart_data=flipkart_data)

if __name__ == '__main__':
    app.run(debug=True)
