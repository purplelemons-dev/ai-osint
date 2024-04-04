from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Truepeoplesearch.com


class TPS:
    def __init__(self):
        # init driver
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.truepeoplesearch.com/")
        self.driver = driver

    def get_all_info(
        self,
        name: str = None,
        phone: str = None,
        email: str = None,
        address: str = None,
    ):
        pass

    def by_name(self, name: str, location: str = None):
        pass

    def by_phone(self, phone: str):
        pass

    def by_address(self, address: str):
        pass

    def by_email(self, email: str):
        pass
