import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

def wait_element(driver, delay=5, by=By.TAG_NAME, value=None):
    return WebDriverWait(driver, delay).until(expected_conditions.presence_of_element_located((by, value)))

def log_into_yandex(driver):
    element = driver.find_element(value='passp-field-login')
    element.send_keys('my_email@yandex.ru')
    login_button = driver.find_element(value='passp:sign-in')
    login_button.click()
    # element = wait_element(driver, delay=3, by=By.ID, value=None)
    time.sleep(5)
    element = driver.find_element(value='passp-field-passwd')
    element.send_keys('my_password')
    login_button = driver.find_element(value='passp:sign-in')
    login_button.click()
    time.sleep(5)
    return driver.current_url

def get_driver(host):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(host)
    time.sleep(5)
    return driver


my_driver = get_driver('https://passport.yandex.ru/auth')
result_url = log_into_yandex(my_driver)
print(result_url)
pass

