from selenium.webdriver.common.by import By

class FinalPage:
    def __init__(self, driver):
        self.driver = driver


    def verify_contact (self, user_data):
        name_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]')
        email_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[1]/div[3]')
        assert name_element.text == user_data["full_name"], f"Expected full name {user_data['full_name']} but got {name_element.text}"
        assert email_element.text == user_data["email"], f"Expected email {user_data['email']} but got {email_element.text}"

    def verify_address (self, user_data):
        name_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[1]')
        address_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[2]')
        code_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]')
        phone_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[4]')
        assert name_element.text == user_data["full_name"], f"Expected full name {user_data['full_name']} but got {name_element.text}"
        assert address_element.text == user_data["address"], f"Expected address {user_data['address']} but got {address_element.text}"
        assert code_element.text.split(", ")[0] == user_data["postcode"], f"Expected postcode {user_data['postcode']} but got {code_element.text}"
        assert phone_element.text == user_data["telephone"], f"Expected telephone {user_data['telephone']} but got {phone_element.text}"

    def verify_item(self):
        quantity_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[2]/div/div[2]/div[1]/div/div[1]')
        assert quantity_element.text == "3 items", f"Expected quantity 3 but got {quantity_element.text}"
        