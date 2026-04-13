from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FormHelpers:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------------- Waits ----------------
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    
    def click(self, locator):
        self.wait_for_clickable(locator).click()
          
    def input_text(self, locator, value): 
        element = self.wait_for_clickable(locator)
        element.clear()            
        element.send_keys(value)
        
    def js_click(self, locator):
    
        element = self.wait_for_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)
        
    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        
    

    