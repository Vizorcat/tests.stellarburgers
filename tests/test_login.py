from locators.locators import Locators

class TestLogin:
    def test_login_via_main_page(driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("artempavlov14a666@yandex.ru")
        driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("12345678")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url