from pages.price_page import PricePage
from libs.base_page import BasePage

import time
import allure

class PriceFlow(PricePage):
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.driver = driver

    def wait_for_new_page(self):
        time.sleep(5)
        print(f"Redirigido a la página")
    
    def validate_http_status(self, url):
        status_code = self.page.get_status_code(url)
        assert status_code == 200, f"HTTP Error: status code {status_code}"

    def select_basic_price(self):
        self.page.click_element(self.OPTION_PRICE_BUTTON)
        self.page.click_element(self.SELECT_PRICE_BUTTON)
        self.validate_http_status(self.driver.current_url)
        
        try:
            self.page.click_element(self.CONTINUE_BUTTON)
            self.validate_http_status(self.driver.current_url)
            print('basic price')
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error interactuando con el elemento: {e.msg}")
            
  