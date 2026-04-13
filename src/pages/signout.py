from selenium.webdriver.common.by import By
from utils.selenium_helpers import FormHelpers
import time

class SignOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = FormHelpers(driver)

        # ---------------- LOCATORS ----------------
        self.profile_menu = (By.CSS_SELECTOR, "button.profile-gradient-ring")
        self.sign_out_btn = (By.XPATH, "//button[text()='Sign Out']")
        
        self.sign_in_nav = (By.XPATH, "//button[text()='Sign in']")

    def sign_out(self):
        
        self.helpers.click(self.profile_menu)
        time.sleep(3)
        self.helpers.js_click(self.sign_out_btn)
        print("Sign Out button clicked")
   

        
        
