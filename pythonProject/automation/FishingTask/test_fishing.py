import sys
import os
from selenium import webdriver
import pytest

from LocatorsPage import Locators
from TestDataPage import TestsData
from MethodsPage import Methods

testdata = TestsData
locator = Locators


def test_fishing():
    driver = TestsData.driver
    username = TestsData.username
    password = TestsData.password
    url = f"https://{username}:{password}@qahiringtask.dev.fishingbooker.com"

    driver.get(url)
    driver.maximize_window()

    method = Methods(driver)
    method.refresh_page()
    method.import_place(testdata.place)
    method.check_need_to_click_next_month()
    method.click_first_enabled_day()
    method.adult_children()
    method.filtering()

    method.angler_choice()

    ### Wait for the new window or tab ###

    method.wait_new_window_or_tab()
    method.message_to_cap()

    method.message()
    method.return_drv()
    driver.quit()
