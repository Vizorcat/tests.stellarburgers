import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

import pytest
from generators.data_generators import generate_email, generate_password

@pytest.fixture
def credentials():
    email = generate_email()
    password = generate_password(10)
    return {"email": email, "password": password}