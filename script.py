#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib
import pandas as pd
import time
import numpy

# Function to fetch price
def get_amazon_price(url):
    website=url
    path = 'C:/Program Files/chromedriver-win64/chromedriver.exe'
    service = Service(executable_path=path)  # selenium 4
    driver = webdriver.Chrome(service=service)
    driver.get(website)
    driver.maximize_window()
    time.sleep(20)
    price = driver.find_elements(by="xpath", value='//div[@class="a-section a-spacing-none aok-align-center aok-relative"]/span/span/span[@class="a-price-whole"]')
    for x in range(len(price)):
        return price[x].text

    return None

# Function to send email
def send_email(subject, body, to_email, from_email, password):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(from_email, to_email, message)

# Main script
def monitor_price(url, desired_price, email_config):
    price = numpy.int64(get_amazon_price(url))
    print(type(price))
    print(type(desired_price))
    if price and price <= numpy.int64(desired_price):
        subject = "Price Alert!"
        body = f"The price for your product has dropped to {price}.\nCheck it here: {url}"
        send_email(subject, body, **email_config)
# Amazon product URL and desired price
input=pd.read_csv("input.csv")
print(input)
url = input["url"]
desired_price = input["desired_price"]  # Desired price to get an alert

# Headers to mimic browser
#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#}

# Email configuration
email_config = {
    "to_email": "l2studiosubusiness@gmail.com",
    "from_email": "l2studiosubusiness@gmail.com",
    "password": "zskv jvpf mqex nrvm"
}

# Run the script
for i in range(len(url)):
    monitor_price(url[i], desired_price[i], email_config)
