import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver import ActionChains

desired_cap={
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appPackage": "com.ATG.World",
    "appWaitDuration": "5000",
    "appExecTimeout": "50000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "app" : "E:\\APK Test\\NEW_SIGNUP_APK_PVT_BUILD_app-debug.apk",
    "autoGrantPermission" : "true"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

driver.find_element_by_id('com.ATG.World:id/getStartedTv').click()
driver.find_element_by_id('com.ATG.World:id/login_email').click()

#login
def test_LoginWithRightCredential(self):
    email = driver.find_element_by_id("com.ATG.World:id/email")
    email.send_keys("wiz_saurabh@rediffmail.com")
    password = driver.find_element_by_id("com.ATG.World:id/password")
    password.send_keys("Pass@123")
    signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
    signin.click()
    print("test_LoginWithRightCredential passed")

test_LoginWithRightCredential(driver)




user_action =TouchAction(driver)
time.sleep(3)

def gotIt(self):
    actions = TouchAction(driver)
    actions.tap(x=172, y=878, count=1).perform()
    print("gotIt")

gotIt(driver)
time.sleep(3)

def gotIt1(self):
    actions1 = TouchAction(driver)
    actions1.tap(x=182, y=1232, count=1).perform()
    print("gotIt_success")

gotIt1(driver)
time.sleep(3)


user_action.tap(x=530, y=1913, count=1).release().perform()

time.sleep(2)
user_action.tap(x=722, y=833, count=1).release().perform()
print("new Photo post")

for i in range(2):
     driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
     time.sleep(2)

#take a photo
driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]").click()
time.sleep(3)
driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
time.sleep(2)
driver.find_element_by_id("com.android.camera2:id/done_button").click()
time.sleep(2)
#driver.find_element_by_id("com.ATG.World:id/button5").click()

caption = driver.find_element_by_id("com.ATG.World:id/postCaption")
caption.send_keys("New test case")
time.sleep(2)
driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
print("new photo posting, success")







