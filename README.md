Page Objetc Model with integration of Pytest
  conf.ini >> Contains all the required locators
  AllureReport >> Contains generated allure report
  ExcelSheet >> Folder contains Excel sheet which contains login credential for the amazon
  Logs >> Contains log information which is having time stamp with the intraction of the element info
  Pages:
    BasePage >> Contains all the required method like click , sendkeys , get _text etc
    amazon >>Page contains all the methods those are required for the testing actions
    LoginPage >> login Page contais Login method which take username and password as arguments
  TestCases:
    conftest.py >> having the driver method which is yielding the driver and perform basic task which is pre-requisite for the every test case
                >> Contains hookimpl which help to create the customise allure report with attached failure screenshot
    Basetest >> which insure fixture implementation at each testcase
    test_Login.py >> validate Login test cases with positive and negative senario
    test_amazon.py >> contains rest test cases like selectibg electronic and dell and validattion 
  Utilities Folder:
    confreader >> Help to parse conf.ini file and provide the required locator
    dataprovider >> Reads the excel file and provide required data 
    LogUtil >> Helps to provide the logging info
