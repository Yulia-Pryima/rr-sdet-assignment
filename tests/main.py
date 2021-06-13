import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from steps.common import login, get_welcome_message, logout
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/yuliapryima/PycharmProjects/Rapyuta Robotics/browser_drivers/chromedriver')
        self.driver.get('http://inst-lvexrslscwtpbksiisccxojt-tdnjyu.ep-r.io/')
        self.wait = WebDriverWait(self.driver, 25)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_map(self):
        driver = self.driver
        expected_organization_name = 'autobootstrap'

        # Log In
        login(self.driver)

        # Select Map
        driver.find_element_by_xpath('//*[@id="app-container"]/div/div[1]/a[3]').click()
        sleep(2)
        organizationName = driver.find_element_by_xpath(
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
        action = webdriver.common.action_chains.ActionChains(driver)
        # position: relative; width: 806px; height: 322px;
        node1 = action.move_to_element_with_offset(el, 900, 300)
        action.click()
        action.perform()
        print('Node1 added.')

        node2 = action.move_to_element_with_offset(el, 1000, 300)
        action.click()
        action.perform()
        print('Node2 added.')

        node3 = action.move_to_element_with_offset(el, 1000, 400)
        action.click()
        action.perform()
        sleep(2)
        print('Node3 added.')

        # Delete nodes
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/a').click()
        node3.send_keys(Keys.DELETE).click().perform()
        sleep(2)
        print('Node3 deleted.')

        # Add edges
        driver.find_element_by_xpath(
            '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/a'
        ).click()
        sleep(2)

        node1.click().perform()
        sleep(2)
        node2.click().perform()
        sleep(2)
        print('Edge added.')

        # # Delete edges
        # driver.find_element_by_xpath(
        #     '//*[@id="app-container"]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/a'
        # ).click()
        #
        # node1.click()
        # node1.send_keys(Keys.DELETE)
        # node1.perform()
        # sleep(2)
        #
        # print('Edge deleted.')

        # Add region

        # Edit region: Move or Change coordinates

        # Log out
        logout(self.wait, driver)

        # Tests
        self.assertEqual(expected_organization_name, organizationName)
        print('"expected_organization_name" = "organizationName"')


if __name__ == '__main__':
    unittest.main()