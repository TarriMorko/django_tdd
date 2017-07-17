from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://localhost:8000')
assert 'Django' in driver.title
