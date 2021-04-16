from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'sderyaginviktor@gmail.com'
passwordStr = '123456'

browser = webdriver.Chrome()
browser.get('http://tbmdevelopment.com/login.php')

# fill in username and hit the next button


username = browser.find_element_by_name('email')
username.send_keys(usernameStr)
password = browser.find_element_by_name('password')
password.send_keys(passwordStr)
nextButton = browser.find_element_by_class_name('btn-primary')
nextButton.click()

print(browser.page_source)
# wait for transition then continue to fill items

# password = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located((By.NAME, "password")))

# password.send_keys(passwordStr)

# signInButton = browser.find_element_by_id('passwordNext')
# signInButton.click()
