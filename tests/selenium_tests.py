import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_login_button(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000")
        t = driver.find_element_by_class_name('AuthButton')
        assert t.is_displayed()
        assert not t.is_selected()
        assert t.text == 'Login by VK'

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:3000")
        t = driver.find_element_by_class_name('AuthButton')
        t.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        l = driver.find_element_by_class_name('oauth_form_input')
        l.send_keys('kyzyloolk@mail.ru')
        time.sleep(1)
        p = driver.find_element_by_name('pass')
        p.send_keys('Jeumiw3i')
        time.sleep(1)
        p.submit()
        time.sleep(1)
        profile = driver.find_element_by_class_name('ProfileDiv')
        assert profile.text == 'You entered as Кежик Кызыл-оол'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()