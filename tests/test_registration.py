from locators.locators import Locators

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_FIELD).send_keys("test1234")
    driver.find_element(*Locators.EMAIL_FIELD).send_keys("testtest1234@gmail.com")
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys("12345678")
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

def test_registration_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_FIELD).send_keys("ТестРег2")
    driver.find_element(*Locators.EMAIL_FIELD).send_keys("testreg2@yandex.ru")
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123")
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    error_message = driver.find_element(*Locators.REGISTRATION_ERROR).text
    assert "Некорректный пароль" in error_message