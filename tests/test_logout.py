from locators.locators import Locators

def test_logout_from_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("testtesttest@gmail.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("testtest")
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGOUT_BUTTON).click()

    assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url