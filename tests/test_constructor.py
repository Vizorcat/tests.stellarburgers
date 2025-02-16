from locators.locators import Locators

def test_constructor_buns_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*Locators.BUNS_SECTION).click()
    is_buns_active = driver.find_element_by_xpath('//*[@id="root"]/div/main/section[1]/div[1]/div[1]').get_attribute("class")
    assert "tab_tab_type_current" in is_buns_active, "Булки"

def test_constructor_sauces_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*Locators.SAUCES_SECTION).click()
    is_sauces_active = driver.find_element_by_xpath('//*[@id="root"]/div/main/section[1]/div[1]/div[2]').get_attribute("class")
    assert "tab_tab_type_current" in is_sauces_active, "Соусы"

def test_constructor_fillings_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*Locators.FILLINGS_SECTION).click()
    is_fillings_active = driver.find_element_by_xpath('//*[@id="root"]/div/main/section[1]/div[1]/div[3]').get_attribute("class")
    assert "tab_tab_type_current" in is_fillings_active, "Начинки"