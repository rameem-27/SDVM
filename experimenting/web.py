from selenium import webdriver
from selenium.webdriver.common.by import By
import os

options = webdriver.FirefoxOptions()
options.add_argument("--kiosk")
driver = webdriver.Firefox(options=options)
