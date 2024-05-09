import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BaseClass


class Amazon(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def select_electronic(self):
        drp = self.selectFromDropdown("search_dropDown_xpath")
        options = drp.options
        for option in options:
            if option.text == "Electronics":
                option.click()
                break

    def get_allElementFromAmazonSearch(self):
        search_ele = []
        elements = self.get_ele_from_list("h3_search_css")
        for ele in elements:
            search_ele.append(ele.text)

        return search_ele

    def select_Amazon(self):
        elements = self.get_ele_from_list("h3_search_css")
        for ele in elements:
            if ele.text == "Amazon.in":
                ele.click()
                break
        time.sleep(5)

    def EnterSearchItem(self, item_name):
        self.input_text("searchbox_xpath", item_name)
        searchBox = self.get_web_ele("searchbox_xpath")
        searchBox.submit()

    def apply_filter(self, min_val, max_val):
        ele = self.get_web_ele("brand_filter_xpath")
        self.scroll_for_ele(ele)
        time.sleep(10)
        self.click("dell_filter_xpath")
        time.sleep(5)
        self.input_text("minValue_xpath", min_val)
        self.input_text("maxValue_xpath", max_val)
        self.click("go_xpath")
        time.sleep(5)

    def validate_productsPrice(self):

        items = self.get_ele_from_list("items_css")
        for item in items:
            price_element = item.find_element(By.XPATH, ".//following::span[@class='a-price-whole']")
            price = int(price_element.text.replace(",", ""))
            if not (30000 <= price <= 50000):
                print(f"Error: {item.text} - Price: {price}")

    def validateAndAddFiveStarItem(self):
        all_fiveStarRatingProduct = []
        rating_items = self.get_ele_from_list("five_rating_xpath")
        for ele in rating_items:
            ele_name = ele.find_element(By.XPATH, ".//preceding::h2[1]")
            all_fiveStarRatingProduct.append(ele_name)
        return all_fiveStarRatingProduct

    def add_toCart(self):
        rating_items = self.get_ele_from_list("five_rating_xpath")
        for item in rating_items:
            name = item.find_element(By.XPATH, ".//preceding::h2[1]")
            print(name.text)
            add_cart = item.find_element(By.XPATH, ".//following::div[@data-csa-c-action-name='addToCart']")

            add_cart.click()
            time.sleep(5)

    def validate_cart(self):
        self.click("cart_css")
