from locators.locators import Locators

class TestLogin:
    def test_login_with_generated_credentials(driver, credentials):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys(credentials["email"])
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys(credentials["password"])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url
