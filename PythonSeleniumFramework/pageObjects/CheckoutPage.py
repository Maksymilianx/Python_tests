from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    divButton = (By.XPATH, "div/button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getDivButton(self):
        return self.driver.find_elements(*CheckOutPage.divButton)

    def getCheckOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
