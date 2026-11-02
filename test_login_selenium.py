"""
Selenium Automation Test Suite for LMS Login Page
Uses suitable locators (By.ID) and explicit waits (WebDriverWait & expected_conditions)
to verify:
  1. Successful login scenario
  2. Invalid credentials error message scenario
"""

from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Initializes a headless Chrome browser session."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver_instance = webdriver.Chrome(options=options)
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(autouse=True)
def open_login_page(driver):
    """Navigates to the local login.html page before each test."""
    login_html_path = Path(__file__).parent.resolve() / "login.html"
    driver.get(login_html_path.as_uri())


def test_successful_login(driver):
    """
    Test 1: Verify successful login with valid credentials.
    Uses By.ID locators and explicit wait for message visibility and text.
    """
    wait = WebDriverWait(driver, timeout=5)

    # 1. Locate elements using suitable By.ID locators
    username_field = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    # 2. Enter valid credentials
    username_field.clear()
    username_field.send_keys("librarian")
    password_field.clear()
    password_field.send_keys("LMS@pass2026")

    # 3. Click the login button
    login_button.click()

    # 4. Explicit wait for the status message element to become visible and display the expected text
    status_element = wait.until(
        EC.visibility_of_element_located((By.ID, "status-message"))
    )
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "status-message"),
            "Login successful! Welcome to the Library Management System."
        )
    )

    # 5. Assertions on text and success class
    assert "Login successful" in status_element.text
    assert "success-msg" in status_element.get_attribute("class")


def test_invalid_credentials_message(driver):
    """
    Test 2: Verify error message when invalid credentials are provided.
    Uses By.ID locators and explicit wait for error message visibility.
    """
    wait = WebDriverWait(driver, timeout=5)

    # 1. Locate elements
    username_field = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    # 2. Enter invalid credentials
    username_field.clear()
    username_field.send_keys("wrong_user")
    password_field.clear()
    password_field.send_keys("invalid_pass")

    # 3. Click the login button
    login_button.click()

    # 4. Explicit wait for error message to appear
    status_element = wait.until(
        EC.visibility_of_element_located((By.ID, "status-message"))
    )
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "status-message"),
            "Invalid credentials. Please check your username or password."
        )
    )

    # 5. Assertions on error message content and styling class
    assert "Invalid credentials" in status_element.text
    assert "error-msg" in status_element.get_attribute("class")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
