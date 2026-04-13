from pages.create import CreateSongs
from pages.signout import SignOutPage


def test_creating_songs(musicGPT_signup_func):
    driver, user_data = musicGPT_signup_func

    create_page = CreateSongs(driver)
   
    create_page.navigate_to_create_songs()
    
     # optional assertion
    assert "/create" in driver.current_url
    
   

   
    
    
    
  