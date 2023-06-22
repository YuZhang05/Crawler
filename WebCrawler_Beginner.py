#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.amazon.com/s?k=jellycat+bunny&sprefix=jellycat%2Caps%2C111&ref=nb_sb_ss_ts-doa-p_3_8" #Replace with the URL of the Airbnb web page you want to scrape

# Configure the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser

# Load the web page
driver.get(url)

# Get the rendered HTML content
html_content = driver.page_source

# Save the HTML content to a file
with open("page.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# Close the browser
driver.quit()

# Load the HTML content
soup = BeautifulSoup(html_content, "html.parser")

data = {"Item_Name":[], "Image_Link":[], "Rating":[], "Price":[]}

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all item containers
item_containers = soup.find_all('div', class_='s-card-container')

# Iterate over each item
for item in item_containers:
    # Extract the title of the item
    title_element = item.find('h2', class_='a-size-mini')
    title = title_element.get_text(strip=True)

    # Extract the image source
    image_element = item.find('img', class_='s-image')
    image_src = image_element['src']

    # Extract the rating
    rating_element = item.find('span',class_='a-icon-alt')
    rating = rating_element.get_text(strip=True)

    # Extract the price
    price_element = item.find('span', class_='a-offscreen')
    price = price_element.get_text(strip=True)
    
    #Save data
    data["Item_Name"].append(title)
    data["Image_Link"].append(image_src)
    data["Rating"].append(rating)
    data["Price"].append(price)

df = pd.DataFrame(data)
df.to_csv("Sample_data.csv")
df.head()

