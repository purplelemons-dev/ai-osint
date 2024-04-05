from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import fake_useragent

# Truepeoplesearch.com


class TPS:
    def __init__(self):
        ua = fake_useragent.FakeUserAgent()
        # init driver
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"user-agent={ua.random}")
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        self.sleep_time = 1

    def get_all_info(
        self,
        name: str = None,
        phone: str = None,
        email: str = None,
        address: str = None,
    ):
        pass

    def by_name(self, name: str, citystatezip: str = None):
        self.driver.delete_all_cookies()
        self.driver.get(
            f"https://www.truepeoplesearch.com/results?{name=}"
            + (f"&{citystatezip=}" if citystatezip is not None else "")
        )
        # sleep to let the page load
        time.sleep(self.sleep_time)
        print(self.driver.current_url)
        suspected_URLs = [
            element.find_element(By.TAG_NAME, "a").get_attribute("href")
            for element in self.driver.find_elements(By.CLASS_NAME, "card-summary")
        ]
        results = []
        print(suspected_URLs)
        for url in suspected_URLs:
            self.driver.get(url)
            time.sleep(self.sleep_time)
            result = (
                self.driver.find_element(By.ID, "personDetails")
                .text.replace("\n", " ")
                .replace("  ", " ")
            )
            results.append(result)
        return results

    def by_phone(self, phone: str):
        pass

    def by_address(self, address: str):
        pass

    def by_email(self, email: str):
        pass


if __name__ == "__main__":
    from .env import TEST_INFO

    tps = TPS()
    print(tps.by_name(TEST_INFO.name, TEST_INFO.location))
    print(tps.by_phone(TEST_INFO.phone))
    print(tps.by_email(TEST_INFO.email))
