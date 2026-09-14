import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@allure.feature("Поиск в Wikipedia")
@allure.story("Поиск статьи")
@allure.title("Поиск статьи 'Россия'")

def test_search():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
        driver.maximize_window()
    
    with allure.step("Открыть сайт Wikipedia"):
        driver.get("https://ru.wikipedia.org")
    
    with allure.step("Ввести слово 'Россия' в поле поиска"):
        search = driver.find_element(By.ID, "searchInput")
        search.send_keys("Россия")
    
    with allure.step("Нажать Enter"):
        search.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    
    with allure.step("Проверить заголовок статьи"):
        heading = wait.until(expected_conditions.visibility_of_element_located((By.ID, "firstHeading")))
        assert "Россия" in heading.text

    with allure.step("Сделать скриншот"):
        driver.save_screenshot("screenshot.png")
        allure.attach.file("screenshot.png", name="Скриншот страницы", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Закрыть браузер"):
        driver.quit()