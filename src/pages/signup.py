from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_helpers import FormHelpers
import random
import string


class SignUpPage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.helpers = FormHelpers(driver) 
        self.wait = WebDriverWait(driver, timeout)

        self.sign_in = (By.XPATH, "//button[text()='Sign in']")
        self.switch_to_signup = (By.XPATH, "//button[contains(text(),'Sign up')]")
        self.email_input = (By.XPATH, "//input[@placeholder='Email']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.sign_up_btn = (By.XPATH, "//button[@type='submit' and text()='Sign Up']")
        self.sign_in_btn = (By.XPATH, "//button[text()='Sign In']")


    def load(self, url):
        self.driver.get(url)


    def signup(self):
        email, password = self._generate_user()
        self.helpers.js_click(self.sign_in)
        self.helpers.click(self.switch_to_signup)
        self.helpers.input_text(self.email_input, email)
        self.helpers.input_text(self.password_input, password)
        self.helpers.js_click(self.sign_up_btn)

        # Return user data (IMPORTANT for tests)
        return {
            "email": email,
            "password": password
        }
        
        
    def _generate_user(self):
        name = ''.join(random.choices(string.ascii_letters, k=6))
        return f"{name.lower()}@gmail.com", "Test@1234"
       

        
        
