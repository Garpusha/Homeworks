import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

def wait_element(driver, delay=5, by=By.TAG_NAME, value=None):
    return WebDriverWait(driver, delay).until(expected_conditions.presence_of_element_located((by, value)))

host = 'https://passport.yandex.ru/auth'
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(host)
element = driver.find_element(value='passp-field-login')
element.send_keys('my_email@yandex.ru')
login_button = driver.find_element(value='passp:sign-in')
login_button.click()
# element = wait_element(driver, delay=3, by=By.ID, value=None)
time.sleep(5)
element = driver.find_element(value='passp-field-passwd')
element.send_keys('mysecretpassword')
login_button = driver.find_element(value='passp:sign-in')
login_button.click()
print(element)
pass
