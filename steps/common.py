from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def login(driver, username='autobootstrap', password='autobootstrap'):
    driver.find_element_by_xpath('//*[@id="app-container"]/div/div/form/div[1]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="app-container"]/div/div/form/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="app-container"]/div/div/form/button').click()
    sleep(2)
    print('User logged in.')


def get_welcome_message(driver):

    return WebDriverWait(driver, 2).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app-container"]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/button/img'))).text


def logout(wait, driver):
    driver.find_element_by_xpath('//*[@id="app-container"]/div/div/div[1]/div/div[2]/div[2]').click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="app-container"]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/ul/li[3]'))).click()
    sleep(2)
    print('User logged out.')


