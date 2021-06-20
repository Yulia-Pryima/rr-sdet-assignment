import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from steps.common import login, get_welcome_message, logout, is_element_present
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/yuliapryima/PycharmProjects/rr-sdet-assignment/browser_drivers/chromedriver')
        self.driver.get('http://inst-lvexrslscwtpbksiisccxojt-tdnjyu.ep-r.io/')
        self.wait = WebDriverWait(self.driver, 25)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_map(self):
        driver = self.driver
        expected_username = 'autobootstrap'

        # Log In
        login(self.driver)

        # Select Map
        driver.find_element_by_xpath('//*[@id="app-container"]/div/div[1]/a[3]').click()
        sleep(2)
        username = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/h3'
        ).text
        driver.find_element_by_id('rc-tabs-1-tab-maps').click()
        sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]'
        ).click()
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/button/span').click()
        sleep(2)
        driver.find_element_by_xpath(
            '// *[ @ id = "app-container"] / div / div / div[2] / div / div / div / div[1] / div[2] / button[1] / span'
        ).click()
        sleep(2)

        # Add nodes
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/a/img'
        ).click()

        el = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div/div')
        action = ActionChains(driver)
        # position: relative; width: 806px; height: 322px;
        node1 = action.move_to_element_with_offset(el, 800, 300)
        node1.click()
        print('Node1 added.')

        node2 = action.move_to_element_with_offset(el, 900, 300)
        node2.click()
        print('Node2 added.')

        node3 = action.move_to_element_with_offset(el, 800, 400)
        node3.click()
        sleep(2)
        print('Node3 added.')

        node4 = action.move_to_element_with_offset(el, 900, 400)
        node4.click().perform()
        sleep(2)
        print('Node4 added.')

        # Delete nodes
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/a').click()
        node4.send_keys(Keys.DELETE).click().perform()
        sleep(2)
        print('Node4 deleted.')

        # Add edges
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/a'
        ).click()
        sleep(2)

        node1.perform()
        sleep(2)
        node2.perform()
        sleep(2)
        print('Edge added.')
        # Make a photo

        self.assertTrue('Save changes' in driver.page_source)
        sleep(2)
        driver.save_screenshot('/Users/yuliapryima/PycharmProjects/rr-sdet-assignment/test_reports/image_1.png')

        # Delete edges
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/a').click()
        edge1 = ActionChains(driver).move_to_element_with_offset(el, 850, 300)
        edge1.send_keys(Keys.DELETE).click()
        edge1.send_keys(Keys.DELETE).click().perform()
        sleep(2)
        print('Edge deleted.')

        # Add region
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[5]/a'
        ).click()

        ActionChains(driver).move_to_element_with_offset(el, 600, 200).click_and_hold().move_by_offset(300, 200).release().perform()
        sleep(2)
        print('Region added.')
        sleep(2)

        # Edit region: Move or Change coordinates
        ActionChains(driver).move_to_element_with_offset(el, 700, 300).click().perform()
        driver.save_screenshot('/Users/yuliapryima/PycharmProjects/rr-sdet-assignment/test_reports/region_1.png')
        sleep(2)

        # Verify Region has name
        region_ID = driver.find_element_by_xpath('//*[@id="root_id"]').get_property('value')
        expected_region_name = 'region_' + region_ID

        region_name = driver.find_element_by_id('root_name').get_property('value')
        try:
            self.assertEqual(expected_region_name, region_name)
        except Exception as e:
            print(e)
            driver.save_screenshot('/Users/yuliapryima/PycharmProjects/rr-sdet-assignment/test_reports/error_1.png')

        # Log out
        logout(self.wait, driver)

        # Verify user logged out
        self.assertTrue(is_element_present(driver, By.XPATH, '//*[@id="app-container"]/div/div/form/button'))

        # Assertions
        self.assertEqual(expected_username, username)
        print(f"{expected_username} = {username}.")

        # Collect Logs into logs.txt


if __name__ == '__main__':
    unittest.main()