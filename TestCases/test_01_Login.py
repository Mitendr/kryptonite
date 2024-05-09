import time

import pytest
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Pages.LoginPage import Login
from Pages.amazon import Amazon

# @pytest.mark.skip
class Test_Login(BaseTest):
    #Negative and positive cases can be tested as per the data provided in excel sheet
    @pytest.mark.parametrize("name,password", dataProvider.get_data("Login"))
    def test_01_InvalidLoginTest(self, name, password):
        Launch_amazon=Amazon(self.driver)
        SignIN = Login(self.driver)
        Launch_amazon.select_Amazon()
        SignIN.login_to_amazon(name,password)