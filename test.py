from selenium import webdriver
from selenium.webdriver.common.by import By
import time
    
driver = webdriver.Chrome()
driver.get("https://b2c.passport.rt.ru")
driver.maximize_window()

time.sleep(3)

login_tab = driver.find_element(By.ID, "t-btn-tab-login")
login_tab.click()

time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys("test_user")

password = driver.find_element(By.ID, "password")
password.send_keys("test_password")

login_btn = driver.find_element(By.ID, "kc-login")
login_btn.click()

time.sleep(2)

error_msg = driver.find_element(By.TAG_NAME, "h2")
assert "Ваш запрос был отклонен из соображений безопасности" in error_msg.text

print("Тест прошёл успешно!")
driver.quit()