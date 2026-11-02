import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000/login")
    yield driver
    driver.quit()

def test_successful_login(driver):
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "username").send_keys("librarian")
    driver.find_element(By.ID, "password").send_keys("LMS@pass2026")
    driver.find_element(By.ID, "login-btn").click()

    msg = wait.until(EC.visibility_of_element_located((By.ID, "status-message")))
    assert "Login successful" in msg.text

def test_invalid_login(driver):
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "username").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-btn").click()

    msg = wait.until(EC.visibility_of_element_located((By.ID, "status-message")))
    assert "Invalid credentials" in msg.text
