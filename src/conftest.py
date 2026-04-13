import pytest
from utils.driver_factory import get_driver
from pages.signup import SignUpPage
from utils import config

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def musicGPT_signup_func():
    driver = get_driver()
    signup_page = SignUpPage(driver)
    signup_page.load(config.musicGPT_URL)
    user_data = signup_page.signup()
    yield driver, user_data
    driver.quit()   
    

