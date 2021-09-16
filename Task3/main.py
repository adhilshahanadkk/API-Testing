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



driver = webdriver.Chrome(executable_path ="c:\selenium webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.atg.party")

assert "ATG" in driver.title
driver.find_element_by_link_text("Login").click()
#log=driver.current_url
time.sleep(3)


def Login(self):
    emailId = driver.find_element_by_id("email_landing")
    emailId.send_keys("wiz_saurabh@rediffmail.com")
    password = driver.find_element_by_id("password_landing")
    password.send_keys("Pass@123")
    #   wait = WebDriverWait("driver,10")until (EC.presence_of_element_located((By.ID)))
    driver.find_element_by_xpath("//*[@id='frm_landing_page_user_login']/div[3]/button").click()
    print("Login -successfully done")

Login(driver)
time.sleep(10)

def Profile(self):
    driver.find_element_by_xpath("//*[@id='dropdownMenuButton']/div[2]/p/span[1]").click()
    time.sleep(3)
    driver.find_element_by_css_selector("body > div.bodycontent > div.in-head.atg-pt-8.atg-pb-8 > nav > div > div.col-lg-3.col-md-4.col-sm-1.col-2.create_post-user__info__parent > div > div.user__info.atg-pl-sm-24 > div.dropdown.open > div.user__info__dropdown.dropdown-menu > div > a.user__info__dropdown-content__user.atg-p-8.atg-mr-24").click()
    print("Profile page")
    driver.implicitly_wait(5)

    # driver.execute_script("window.scrollBy(0,2000)")
Profile(driver)

#page =driver.find_element_by_tag_name('html')
# page.send_keys(Keys.PAGE_DOWN).perform()

driver.implicitly_wait(3)
#driver.find_element_by_id("postheader").click()
#driver.execute_script("window.scrollTo(0,2000)")
time.sleep(3)
#driver.find_element_by_id("interestheader").click()


def ProfileEditing(self):
    driver.find_element_by_id("edt-prof").click()
    userName = driver.find_element_by_id("new_user_name")
    userName.clear()
    #userName.send_keys(Keys.CLEAR)
    driver.implicitly_wait(5)
    userName.send_keys("bassi_new")
    bio = driver.find_element_by_id("about_me")
    bio.clear()
    bio.send_keys("I live, I learn, I play, I love, I enjoy my life very much.")
    time.sleep(3)
    driver.find_element_by_xpath("// *[ @ id ='account_setting'] / div[10] / button[1]").click()


    #time.sleep(10)


ProfileEditing(driver)


## explicit wait
#w = WebDriverWait(driver, 10).until(ProfileEditing)

driver.implicitly_wait(20)
time.sleep(10)
driver.find_element_by_xpath("//*[@id='dropdownMenuButton']/div[2]/p/span[1]").click()
time.sleep(3)
driver.find_element_by_css_selector("body > div.bodycontent > div.in-head.atg-pt-8.atg-pb-8 > nav > div > div.col-lg-3.col-md-4.col-sm-1.col-2.create_post-user__info__parent > div > div.user__info.atg-pl-sm-24 > div.dropdown.open > div.user__info__dropdown.dropdown-menu > div > a.user__info__dropdown-content__user.atg-p-8.atg-mr-24").click()
driver.implicitly_wait(5)

userNameOrg = driver.find_element_by_xpath("//*[@id='userData']/div/div/div/div[2]/span")
assert "bassi_new" == userNameOrg.text
print("editing successfull")


driver.execute_script("window.scrollTo(0,5000)")
driver.back()


def manage_resume(self):
    resume = driver.find_element_by_xpath("//*[@id='manage_resume']")
    resume.click()
    time.sleep(3)
    print("mange_resume working properly")

manage_resume(driver)

def Applied_Job(self):
    driver.find_element_by_xpath("//*[@id='my_job_student']").click()
    time.sleep(10)
    All = driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/span[1]")
    All.click()
    driver.implicitly_wait(5)
    seen = driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/span[1]")
    seen.click()
    time.sleep(15)
    driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/span[2]/img")
    short_list = driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[3]/div[2]/span[1]")
    short_list.click()
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[3]/div[2]/span[2]/img")
    # selected = driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[4]/div[2]/span[1]")
    # selected.click()
    # time.sleep(10)
    # driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[4]/div[2]/span[2]/img")
    # rejected = driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[5]/div[2]/span[1]")
    # rejected.click()
    time.sleep(10)
   # driver.find_element_by_xpath("//*[@id='content']/section/div[2]/div/div/div[2]/div/div[1]/div[5]/div[2]/span[2]/img")
    more_Job = driver.find_element_by_xpath("//*[@id='recommended_jobs']/div[2]/div/div[2]/div[2]/div[1]/a")
    more_Job.click()
    time.sleep(15)
    driver.back()
    #driver.find_element_by_xpath("//*[@id='recommended_jobs']/div[2]/div/div[2]/div[2]/div[1]/a/img")
    print("job applied part working properly")


Applied_Job(driver)

time.sleep(5)

def Logout(self):
    driver.find_element_by_xpath("//*[@id='wrapper']/div/a[7]").click()
    time.sleep(5)

    s = driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/ul/li[1]/a")
    assert "Sign Up" == s.text
    print("successfully LogOut")

Logout(driver)
##page scrolling
# driver.execute_script("window.scrollTo(0,5000)")
# I=driver.find_element_by_xpath("//*[@id='interestheader']")
# a = ActionChains(driver)
# a.move_to_element(I).perform()

#driver.close()