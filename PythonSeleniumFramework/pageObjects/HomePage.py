from selenium.webdriver.common.by import By

from PythonSeleniumFramework.pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(text(),'Shop')]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop)
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage