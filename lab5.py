from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com"


def test_dropdown():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get(f"{URL}/dropdown")

    dropdown = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))

    select = Select(dropdown)
    select.select_by_visible_text("Option 1")

    selected = select.first_selected_option.text
    assert selected == "Option 1"

    driver.quit()


def test_checkbox():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get(f"{URL}/checkboxes")

    checkboxes = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
    )
    assert len(checkboxes) == 2

    first = checkboxes[0]
    before = first.is_selected()

    first.click()

    after = first.is_selected()
    assert before != after

    driver.quit()


def test_alert():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get(f"{URL}/javascript_alerts")

    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']"))
    )
    button.click()

    alert = wait.until(EC.alert_is_present())

    alert.accept()

    result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
    assert result.text == "You successfully clicked an alert"

    driver.quit()


def test_new_window():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get(f"{URL}/windows")

    original_window = driver.current_window_handle

    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    link.click()

    wait.until(EC.number_of_windows_to_be(2))
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert "New Window" in heading.text

    driver.switch_to.window(original_window)
    assert driver.current_window_handle == original_window

    driver.quit()

if __name__ == "__main__":
    test_dropdown()
    test_checkbox()
    test_alert()
    test_new_window()
    print("Все 4 теста прошли успешно")