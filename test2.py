from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

  
driver = webdriver.Chrome()
driver.get("https://www.kinopoisk.ru/")
driver.maximize_window()

add = driver.find_element(By.XPATH, "//div[8]/div/div/div/button[@class='styles_root__mwAP6']")
add.click()

time.sleep(1)

search = driver.find_element(By.NAME, "text")
search.send_keys("Матрица")
search.send_keys(Keys.ENTER)

time.sleep(2)

page_text = driver.find_element(By.TAG_NAME, "body").text
assert "Матрица" in page_text

print("Тест прошёл успешно!")
driver.quit()