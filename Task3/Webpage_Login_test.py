import time
import unittest

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class pythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path ="c:\selenium webdriver\chromedriver.exe")


    def test_login_profile(self):
        driver = self.driver
        driver.get("http://www.atg.party")
        assert "ATG" in driver.title
        driver.find_element_by_link_text("Login").click()
        driver.implicitly_wait(5)
        emailId = driver.find_element_by_id("email_landing")
        emailId.send_keys("wiz_saurabh@rediffmail.com")
        password = driver.find_element_by_id("password_landing")
        password.send_keys("Pass@123")
        driver.find_element_by_xpath("//*[@id='frm_landing_page_user_login']/div[3]/button").click()



    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()