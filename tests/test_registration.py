import random
import string
from locators.locators import Locators


def generate_email(domain="gmail.com"):
    username_length = 8
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return f"{username}@{domain}"

def generate_password(length=8):
    if length < 4:
        raise ValueError("Пароль должен быть не менее 4 символов.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    random_email = generate_email()
    random_password = generate_password(8)

    driver.find_element(*Locators.NAME_FIELD).send_keys("test1234")
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(random_email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(random_password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

def test_registration_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_FIELD).send_keys("ТестРег2")
    driver.find_element(*Locators.EMAIL_FIELD).send_keys("testreg2@yandex.ru")
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123")
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    error_message = driver.find_element(*Locators.REGISTRATION_ERROR).text
    assert "Некорректный пароль" in error_message