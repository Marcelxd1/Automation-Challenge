from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.purchase_page import PurchasePage
from utils.random_data import generate_user_data
from pages.final_page import FinalPage
import random
import json
import os



import time

def save_user_data(user_data, filename="usuario.txt"):
    # Save random user data in txt
    filepath = os.path.join("src", filename)
    with open(filepath, 'w') as file:
        json.dump(user_data, file, indent=4)

def test_automation():

    # Chrome driver service to automatically install and use the driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Open [Home page]
        driver.get("https://demo.evershop.io/")
        driver.maximize_window()

        # Generate random data
        user_data = generate_user_data()
        print(user_data)

        save_user_data(user_data)

        # Go to sign in
        sign_in_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[3]/a')
        sign_in_button.click()
        time.sleep(2)
        

        # Register
        login_page = LoginPage(driver)
        login_page.create_account()
        login_page.register_user(user_data)
        time.sleep(5)

        # Sign in
        # login_page.click_sign_in()
        # login_page.enter_credentials(user_data)
        # time.sleep(1)
        # login_page.click_sign_in()
        # time.sleep(2)

        # Open [Men / Women page]
        categories = ["Men", "Women"]
        category = random.choice(categories)
        purchase_page = PurchasePage(driver)
        purchase_page.go_to_category(category)

        # # Select 3 products
        purchase_page.add_product('//*[@id="app"]/div/main/div[3]/div[2]/div[2]/div/div[1]/div[1]/a', 5)
        purchase_page.go_to_category(category)
        purchase_page.add_product('//*[@id="app"]/div/main/div[3]/div[2]/div[2]/div/div[2]/div[1]/a', 4)
        purchase_page.go_to_category(category)
        purchase_page.add_product('//*[@id="app"]/div/main/div[3]/div[2]/div[2]/div/div[3]/div[1]/a')


        # Buy selected products
        purchase_page.go_to_purchase()
        purchase_page.enter_shipping_info(user_data)
        purchase_page.payment_method()

        # Verify order
        final_page = FinalPage(driver)
        final_page.verify_address(user_data)
        final_page.verify_contact(user_data)
        final_page.verify_item()


        print("SUCCESS ORDER")
        time.sleep(10)

    
    finally:
        driver.quit()
        

if __name__ == "__main__":
    test_automation()
