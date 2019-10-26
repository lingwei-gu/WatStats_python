from selenium import webdriver


class Scrape(object):
    def __init__(self, account, password):
        self.__account = account
        self.__password = password

    def scrape(self):
        # make sure geckodriver is installed in your package
        driver = webdriver.Firefox(executable_path='geckodriver')
        driver.get("https://watcard.uwaterloo.ca/OneWeb/Account/LogOn")

        # input account number
        elem_user = driver.find_element_by_name("Account")
        elem_user.send_keys(self.__account)

        # input password(PIN)
        elem_pwd = driver.find_element_by_name("Password")
        elem_pwd.send_keys(self.__password)

        # click the logon button
        elem = driver.find_element_by_tag_name("button")
        elem.click()
        # login is finished

        driver.get("https://watcard.uwaterloo.ca/OneWeb/Financial/Transactions")
        elements = driver.find_elements_by_class_name("ow-link")
        elements[1].click()
        elements = driver.find_element_by_id("transaction_result")
        elements.click()
        return driver.page_source




