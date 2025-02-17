from locators.locators import Locators

def test_constructor_buns_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*Locators.BUNS_SECTION).click()
    is_buns_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
    assert "tab_tab_type_current" in is_buns_active, "Ожидалось, что вкладка 'Булки' станет активной, но этого не произошло"

def test_constructor_sauces_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*Locators.SAUCES_SECTION).click()
    is_sauces_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
    assert "tab_tab_type_current" in is_sauces_active, "Ожидалось, что вкладка 'Соусы' станет активной, но этого не произошло."

def test_constructor_fillings_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*Locators.FILLINGS_SECTION).click()
    is_fillings_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
    assert "tab_tab_type_current" in is_fillings_active, "Ожидалось, что вкладка 'Начинки' станет активной, но этого не произошло."