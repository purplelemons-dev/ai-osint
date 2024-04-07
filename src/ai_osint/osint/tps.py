# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import fake_useragent
from selenium.webdriver.common.by import By
from botasaurus import browser, AntiDetectDriver
import time
from typing import Any

# Truepeoplesearch.com


class TPS:

    @browser(block_resources=True, headless=True)
    @staticmethod
    def preload_driver(driver: AntiDetectDriver, data):
        while True:
            try:
                driver.get_google()
                break
            except:
                pass
        return {"status": driver.title}

    def get_all_info(
        self,
        name: str = None,
        phone: str = None,
        email: str = None,
        address: str = None,
    ):
        results = []
        if name is not None:
            results.append(
                self.by_name(metadata={"name": name, "citystatezip": address})
            )
        elif phone is not None:
            results.append(self.by_phone(metadata={"phone": phone}))
        elif email is not None:
            results.append(self.by_email(metadata={"email": email}))
        # elif address is not None:
        #    results.append(self.by_address(address))
        return results

    @browser(block_resources=True, headless=True)
    @staticmethod
    def by_name(
        driver: AntiDetectDriver, data: dict[str, Any], metadata: dict[str, Any]
    ):
        name = metadata["name"]
        citystatezip = metadata["citystatezip"]
        URL = f"https://www.truepeoplesearch.com/results?{name=}" + (
            f"&{citystatezip=}" if citystatezip is not None else ""
        ).replace("'", "")
        driver.get(URL)
        time.sleep(1)
        suspected_URLs = [
            element.find_element(By.TAG_NAME, "a").get_attribute("href")
            for element in driver.find_elements(By.CLASS_NAME, "card-summary")
        ][:4]
        results = []
        for url in suspected_URLs:
            driver.get(url)
            time.sleep(1)
            result = (
                driver.find_element(By.ID, "personDetails")
                .text.replace("\n", " ")
                .replace("  ", " ")
            )
            results.append(result)
        return results

    @browser(block_resources=True, headless=True)
    @staticmethod
    def by_phone(
        driver: AntiDetectDriver, data: dict[str, Any], metadata: dict[str, Any]
    ):
        phoneno = metadata["phone"]
        URL = f"https://www.truepeoplesearch.com/resultphone?{phoneno=}".replace(
            "'", ""
        )
        driver.get(URL)
        time.sleep(1)
        suspected_URLs = [
            element.find_element(By.TAG_NAME, "a").get_attribute("href")
            for element in driver.find_elements(By.CLASS_NAME, "card-summary")
        ][:4]
        results = []
        for url in suspected_URLs:
            driver.get(url)
            time.sleep(1)
            result = (
                driver.find_element(By.ID, "personDetails")
                .text.replace("\n", " ")
                .replace("  ", " ")
            )
            results.append(result)
        return results

    @browser(block_resources=True, headless=True)
    @staticmethod
    def by_address(
        driver: AntiDetectDriver, data: dict[str, Any], metadata: dict[str, Any]
    ):
        raise NotImplementedError
        address = metadata["address"]
        citystatezip = metadata["citystatezip"]
        driver.get(
            f"https://www.truepeoplesearch.com/resultaddress?streetaddress={address}&{citystatezip=}"
        )
        time.sleep(1)
        suspected_URLs = [
            element.find_element(By.TAG_NAME, "a").get_attribute("href")
            for element in driver.find_elements(By.CLASS_NAME, "card-summary")
        ][:4]
        results = []
        for url in suspected_URLs:
            driver.get(url)
            time.sleep(1)
            result = (
                driver.find_element(By.ID, "personDetails")
                .text.replace("\n", " ")
                .replace("  ", " ")
            )
            results.append(result)
        return results

    @browser(block_resources=True, headless=True)
    @staticmethod
    def by_email(
        driver: AntiDetectDriver, data: dict[str, Any], metadata: dict[str, Any]
    ):
        email: str = metadata["email"]
        email = email.replace("@", "_at_")
        email = email.replace(".", "_dot_")

        URL = f"https://www.truepeoplesearch.com/resultemail?{email=}".replace("'", "")
        driver.get(URL)
        time.sleep(1)
        suspected_URLs = [
            element.find_element(By.TAG_NAME, "a").get_attribute("href")
            for element in driver.find_elements(By.CLASS_NAME, "card-summary")
        ][:4]
        results = []
        for url in suspected_URLs:
            driver.get(url)
            time.sleep(1)
            result = (
                driver.find_element(By.ID, "personDetails")
                .text.replace("\n", " ")
                .replace("  ", " ")
            )
            results.append(result)
        return results


if __name__ == "__main__":
    print("Initializing True People Search driver...")

    TPS().preload_driver()
    exit(0)
