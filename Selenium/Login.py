from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
chromeoptions.add_experimental_option("detach", True)
chromedriver = webdriver.Chrome(options = chromeoptions)

chromedriver.get("https://google.com")