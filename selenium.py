import os
pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pythonscratcher.eu.org")

# IFF THIS OPENS IN A "WEBVIEW" CHANGE IT TO "OUTPUT"!

print ("IF THIS OPENS IN A WEBVIEW CHANGE IT TO OUTPUT! BY PRESSING THE + BUTTON (This may take a while if you use Replit free)")
