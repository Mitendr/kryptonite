import time

import pytest

from Utilities.LogUtil import Logger
from TestCases.BaseTest import BaseTest
from Pages.amazon import Amazon
from Utilities import dataProvider


class Test_AmazonProduct(BaseTest):

    def test_printAllAmazonSearchResult(self):
        Search = Amazon(self.driver)
        result = Search.get_allElementFromAmazonSearch()
        print(result)

    def test_click_to_amazon(self):
        Select=Amazon(self.driver)
        Select.select_Amazon()

    def test_select_ElectronicsAndDell(self):
        Dell=Amazon(self.driver)
        Dell.select_Amazon()
        Dell.select_electronic()
        time.sleep(5)
        Dell.EnterSearchItem("Dell Computer")
        time.sleep(5)
        Dell.apply_filter("30000","50000")
        time.sleep(20)

        # Validate all items are in the price range of 30k to 50K
        Dell.validate_productsPrice()

        # Validate 5 start rating products
        Dell.validateAndAddFiveStarItem()
        Dell.add_toCart()

        # validate cart items
        Dell.validate_cart()
        time.sleep(10)
