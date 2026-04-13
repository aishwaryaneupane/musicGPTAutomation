from pages.create import CreateSongs
from pages.topup import TopUpStripe
from pages.signout import SignOutPage


def test_creating_songs_payment(musicGPT_signup_func):
    driver, user_data = musicGPT_signup_func

    create_page = CreateSongs(driver)
    topup_page = TopUpStripe(driver)
    signout_page = SignOutPage(driver)

   
    create_page.navigate_to_create_songs()
    topup_page.navigate_to_topup_amount()
    
    driver.switch_to.default_content()
    
    signout_page.sign_out()
    print("Test complete: User topped up and signed out.")


