# cookies before login and after login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

print("cookies before login")
for cookies in driver.get_cookies():
    print(cookies)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

print(" cookies after login")
for cookies in driver.get_cookies():
    print(cookies)



# Logout
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()

# Wait for the menu to open
time.sleep(2)

logout_link = driver.find_element(By.LINK_TEXT, "Logout")
logout_link.click()

# Wait for the logout process to complete
time.sleep(3)


# Close the browser
driver.quit()