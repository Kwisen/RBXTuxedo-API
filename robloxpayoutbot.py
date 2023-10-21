# This script is based on the Selenium python library, I have annotated this script and explained it to my best.
# Credits: 
# Kyukyaku (Nerability) (Owner of RBX Tuxedo) (Made most of the script)
# Olivezzz (Fixed bugs and added the insufficient robux notificator, dynamic gamepass id (deprecated)(original is the deprecated code above the current gamepass id) and decline cookies button.)
# Ok so, ## = Buggy code that im not fixing yet.

import os # Imports the Operating System
import time
from time import sleep # Imports sleep from time (to wait)

import selenium # Imports Selenium

from dotenv import load_dotenv
from selenium import webdriver # Imports webdriver (crucial to run the script) (this actually opens the webdriver.)
from selenium.webdriver.common.by import By # Imports By (crucial) (to find the element)
from selenium.webdriver.support.ui import WebDriverWait # Imports WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec # Imports ec or expected_conditions (to get expected element/block)
from selenium.common.exceptions import TimeoutException # Imports TimeException (for counter measures)

# Get gamepass ID from user

gamepass_id = (input('Input gamepass ID: ')) # (Deprecated code)

# Replace with your Roblox username and password

roblox_username = ("ElizabethCalderon9")
roblox_password = ("MalitoMalito1")

# Create a WebDriver instance

driver = webdriver.Edge() # Change the webdriver according to your path system and/or default browser agent.

# Open the Roblox website

url = 'https://www.roblox.com/login'
driver.get(url)

# Wait for the login page to load

wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
wait.until(ec.presence_of_element_located((By.ID, 'login-username')))

# Find the login elements and enter username and password

username_field = driver.find_element(By.ID, 'login-username')
password_field = driver.find_element(By.ID, 'login-password')

username_field.send_keys(roblox_username)
password_field.send_keys(roblox_password)

# Decline cookies if asked

try:
    cookie_button = driver.find_element(By.CLASS_NAME, 'btn-secondary-lg')
    cookie_button.click()
except:  # No cookie button / No problem
    pass

# Submit the login form

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

# Wait for login to complete because Roblox login is wayyy to slow

wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.CLASS_NAME, "age-bracket-label-username")))

# Get gamepass ID from user (Buggy code)

## gamepass_link = 'https://pastebin.com/raw/HPxjkBCq'  # Replace with the RAW URL of the website where the RAW text of the gamepass ID is stored at
# In my case, I will be using a gamepass ID to test the script.

# Gets the gamepass link

## driver.get(gamepass_link)

## wait = WebDriverWait(driver, 10) # Adjust as needed
## try:
##     wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'p:contains("https://www.roblox.com/game-pass/")')))
##     element = driver.find_element_by_css_selector("p:contains('https://www.roblox.com/game-pass/')")
##     element = driver.find_element_by_css_selector("p:contains('https://www.roblox.com/game-pass/')")
##     text = element.get_attribute("innerText")
## except TimeoutException:
##     wait.until(ec.presence_of_element_located(By.CSS_SELECTOR, 'p:contains("https://web.roblox.com/game-pass/")'))
## else:
##      url = text

# Navigate to gamepass

url = f'https://www.roblox.com/game-pass/{gamepass_id}' # (Deprecated code)

## url = f'{gamepass_link}'
driver.get(url)

# Add a wait here if the next step requires the page to load

wait = WebDriverWait(driver, 10) # Adjust it as needed (again)
wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'PurchaseButton')))
Purchase = driver.find_element(By.CLASS_NAME, 'PurchaseButton')
Purchase.click()

# Check if there is insufficient Robux

wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.CLASS_NAME, "modal-title")))

modal_title = driver.find_element(By.CLASS_NAME, "modal-title")

# Wait for popup

while modal_title.text in ["", None]:
    sleep(0.1)

if modal_title.text == "Insufficient Robux":
    print("INSUFFICIENT ROBUK!!!!")  # When the robuk is insuficent!
    try: 
            wait = WebDriverWait(driver, 10) # Adjust? Maybe, if your internet slow asf
            wait.until(ec.presence_of_element_located((By.ID, 'confirm-btn')))
            Confirm = driver.find_element(By.ID, 'confirm-btn')
            Confirm.click()
    finally:
        driver.close()
else:
    # Automate to click the confirm buy button

    wait = WebDriverWait(driver, 10) # Adjust? Maybe, if your internet slow asf
    wait.until(ec.presence_of_element_located((By.ID, 'confirm-btn')))
    Confirm = driver.find_element(By.ID, 'confirm-btn')
    Confirm.click()

# Not enough balance (Tester)



# Wait (manual input)



# Closes the webdriver (bot end)

driver.close()