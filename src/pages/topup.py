from selenium.webdriver.common.by import By
from utils.selenium_helpers import FormHelpers 
import time



class TopUpStripe:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = FormHelpers(driver)  
        #LOCATORS 
        
        self.topup_link = (By.XPATH, "//button[contains(text(), 'Top Up')] | //a[contains(text(), 'Top Up')] | //span[text()='Top Up']")    
        
        self.buy_now_btn = (By.XPATH, "//button[text()='Buy Now']")
        
        self.email_field = (By.ID, "email")
        
        self.card_number = (By.ID, "cardNumber")
        
        self.expiry_field = (By.ID, "cardExpiry")
        
        self.card_cvc = (By.ID, "cardCvc")
        
        self.cardholder_name = (By.ID, "billingName")
        
        self.pay_button = (By.CSS_SELECTOR, "button.SubmitButton")


    def navigate_to_topup_amount(self):  

     

        self.helpers.js_click(self.topup_link)

        print("Top Up clicked")

        time.sleep(3)

        self.helpers.js_click(self.buy_now_btn)

        print("Buy Now clicked")

     

        self.helpers.input_text(self.email_field, "test@example.com")

       

        self.helpers.input_text(self.card_number, "4242 4242 4242 4242")

       

        self.helpers.input_text(self.expiry_field, "01/29")

       

        self.helpers.input_text(self.card_cvc, "123")

        self.helpers.scroll_to_element(self.card_cvc)

       

        self.helpers.input_text(self.cardholder_name, "Test")

        self.helpers.scroll_to_element(self.cardholder_name)

       

        self.helpers.js_click(self.pay_button)

        print("Payment submitted")

       
        
        
