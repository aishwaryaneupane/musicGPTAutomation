from pages.signup import SignUpPage
from utils import config
def test_new_signup(driver):

    signup_page = SignUpPage(driver)

    signup_page.load(config.musicGPT_URL)
    
    new_user_data = signup_page.signup()

    assert "@gmail.com" in new_user_data["email"]  


  


   



    

  