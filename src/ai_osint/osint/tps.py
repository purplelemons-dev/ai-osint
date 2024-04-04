from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Truepeoplesearch.com
# init driver
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("https://www.truepeoplesearch.com/")


class TPS:
    def by_name(self, name: str, location: str = None):
        pass

    def by_phone(self, phone: str):
        pass

    def by_address(self, address: str):
        pass

    def by_email(self, email: str):
        pass
