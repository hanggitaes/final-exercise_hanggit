import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import csv

class TestSauceDemo(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
    
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)
        self.assertTrue(inventory_page.is_logged_in())
    
    def test_login_invalid(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "wrong_password")
        self.assertTrue(login_page.is_error_displayed())
    
    def test_add_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_first_item_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.open_cart()
        self.assertTrue(cart_page.is_item_in_cart())
    
    def test_checkout_process(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_first_item_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.open_cart()
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_information("John", "Doe", "12345")
        checkout_page.finish_checkout()
        self.assertTrue(checkout_page.is_checkout_complete())
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()