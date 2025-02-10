from selenium.webdriver.common.by import By

class Locators:

    REGISTER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # Кнопка "Зарегистрироваться"
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") # Поле ввода имени
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # Поле ввода email
    PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input") # Поле ввода пароля
    REGISTRATION_ERROR = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p") # Ошибка при некорректной регистрации

    LOGIN_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # Кнопка "Войти"
    LOGIN_EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") # Поле email для входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # Поле пароля для входа
    ACCOUNT_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") # Кнопка "Личный кабинет"

    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p") #Конструктор
    LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div/a/svg") # Логотип Stellar Burgers

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход"

    BUNS_SECTION = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]") # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span") # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]") # Раздел "Начинки"