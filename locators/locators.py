from selenium.webdriver.common.by import By

class Locators:

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    NAME_FIELD = (By.XPATH, "//input[@name='name']") # Поле ввода имени
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']") # Поле ввода email
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']") # Поле ввода пароля
    REGISTRATION_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']") # Ошибка при некорректной регистрации

    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Войти']") # Кнопка "Войти"
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name='email']")  # Поле email для входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")  # Поле пароля для входа
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет"

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #Конструктор
    LOGO = (By.XPATH, "//a[@href='/']/*[name()='svg']")  # Логотип Stellar Burgers

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"

    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab')]")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab')]")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab')]") # Раздел "Начинки"
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # Активная вкладка (по классу)
