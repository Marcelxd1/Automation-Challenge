from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/button')
        sign_in_button.click()

    def enter_credentials(self, user_data):
        self.driver.find_element(By.NAME, "email").send_keys(user_data["email"])
        self.driver.find_element(By.NAME, "password").send_keys(user_data["password"])

    def create_account(self):
        create_account_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div/div/div/a[1]')
        create_account_button.click()


    def register_user(self, user_data):
        self.driver.find_element(By.NAME, "full_name").send_keys(user_data["full_name"])
        self.driver.find_element(By.NAME, "email").send_keys(user_data["email"])
        self.driver.find_element(By.NAME, "password").send_keys(user_data["password"])
        reg_button = self.driver.find_element(By.XPATH, '//*[@id="registerForm"]/div[2]/button')
        reg_button.click()

