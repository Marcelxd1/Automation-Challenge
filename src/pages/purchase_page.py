from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class PurchasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_category(self, category):
        category_button = self.driver.find_element(By.XPATH, f'//a[contains(text(), "{category}")]')
        category_button.click()
        time.sleep(1)
    
    def go_to_purchase(self):
        purchase_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[2]/a')
        purchase_button.click()
        checkout_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div/div[2]/div/div[2]/div/div[2]/a')
        checkout_button.click()
        time.sleep(1)

    def add_product(self, xpath, quantity=1):

        # Select a product
        product = self.driver.find_element(By.XPATH, xpath)
        product.click()
        time.sleep(1)

        # Select the quantity
        quantity_field = self.driver.find_element(By.NAME, "qty")
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

        # Select variant options
        size_field = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/a')
        size_field.click()
        time.sleep(3)
        color_field = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/a')
        color_field.click()
        time.sleep(3)

        # Click ADD to CART
        add_button = self.driver.find_element(By.XPATH, '//*[@id="productForm"]/div/div/div[2]/button')
        add_button.click()

    def enter_shipping_info(self, user_data):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "address[full_name]"))
        ).send_keys(user_data["full_name"])
        # Fill the inputs
        self.driver.find_element(By.NAME, "address[telephone]").send_keys(user_data["telephone"])
        self.driver.find_element(By.NAME, "address[address_1]").send_keys(user_data["address"])
        self.driver.find_element(By.NAME, "address[city]").send_keys(user_data["city"])
        self.driver.find_element(By.NAME, "address[postcode]").send_keys(user_data["postcode"])

        # Select the country
        country_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "address[country]"))
        )
        select = Select(country_dropdown)
        select.select_by_value(user_data["country"])

        # Select the province
        province_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "address[province]"))
        )
        select_p = Select(province_dropdown)
        select_p.select_by_value(user_data["province"])

        # Select radio button
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkoutShippingAddressForm"]/div[1]/div[6]/div/div/div/div[1]/label'))
        )
        radio_button.click()

        
    def payment_method(self):
        pay_button = self.driver.find_element(By.XPATH, '//*[@id="checkoutShippingAddressForm"]/div[2]/button')
        pay_button.click()

        # Select visa option
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '(//div[@class="flex justify-start items-center gap-1"]/*/*[name()="svg"])[3]'))
        )
        visa_option = self.driver.find_element(By.XPATH, '(//div[@class="flex justify-start items-center gap-1"]/*/*[name()="svg"])[3]')
        visa_option.click()

        # Click on success to get correct card information 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutPaymentForm"]/div[3]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/button[1]'))
        )
        self.driver.find_element(By.XPATH, '//*[@id="checkoutPaymentForm"]/div[3]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/button[1]').click()
        
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutPaymentForm"]/div[3]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]'))
        )

        # Fill card inputs
        card_number_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Test card number')]")
        card_number = card_number_element.text.split(": ")[1]
        card_expiry_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Test card expiry')]")
        card_expiry = card_expiry_element.text.split(": ")[1] # DAte error ----
        card_cvc_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Test card CVC')]")
        card_cvc = card_cvc_element.text.split(": ")[1] 
        card_expiry = "0425" #had to change the year

        iframes = self.driver.find_elements(By.TAG_NAME, 'iframe')
        for i, iframe in enumerate(iframes):
            self.driver.switch_to.frame(iframe)
    
            try:
                # Search card number input
                card_number_field = self.driver.find_element(By.NAME, 'cardnumber')
                card_date_field = self.driver.find_element(By.NAME, 'exp-date')
                card_cvc_field = self.driver.find_element(By.NAME, 'cvc')
                if card_number_field and card_date_field and card_cvc_field:
                    card_number_field.send_keys(card_number)
                    card_date_field.send_keys(card_expiry)
                    card_cvc_field.send_keys(card_cvc)
                    break
            except:
                pass
            
            self.driver.switch_to.default_content()

        self.driver.switch_to.default_content()
        time.sleep(5)
        
        # Complete the purchase
        order_button = self.driver.find_element(By.XPATH, '//*[@id="checkoutPaymentForm"]/div[5]/button')
        order_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/h3'))
        )
        time.sleep(1)
        
        