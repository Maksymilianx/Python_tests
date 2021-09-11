import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utulities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage



class TestOne(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)
        check_out_page = home_page.shopItems()
        products = check_out_page.getCardTitle()
        i = -1
        for product in products:
            i =+ 1
            product_text = product.text
            # productName = product.find_element_by_xpath("div/h4/a").text
            if product_text == "Blackberry":
                check_out_page.divButton()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirm_page = check_out_page.getCheckOutItems()
        self.driver.find_element_by_id("country").send_keys("pol")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Poland")))
        self.driver.find_element_by_link_text("Poland").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText
