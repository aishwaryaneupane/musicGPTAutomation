from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.selenium_helpers import FormHelpers
import time


class CreateSongs:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = FormHelpers(driver)
        
        #LOCATORS 
        time.sleep(5)
        self.prompt = (By.XPATH, "//textarea")     
        self.generate_arrow = (By.XPATH, "//button[contains(@class,'rounded-full')]")
        self.email_initial = ((By.CSS_SELECTOR, "button.profile-gradient-ring"))
        
        
    
    def navigate_to_create_songs(self):             
        prompt_field = self.driver.find_element(*self.prompt)
        prompt_field.send_keys("Generate a birthday song using just guitar, for me ")
    
        # Press Enter instead of clicking the arrow
        prompt_field.send_keys(Keys.ENTER)
        time.sleep(3)
        
        profile_initial = self.driver.find_element(*self.email_initial)
        profile_initial.click()
        
        time.sleep(60)


