from _ast import Assert

import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date

from LocatorsPage import Locators
from TestDataPage import TestsData

testdata = TestsData
locator = Locators


class Methods:

    def __init__(self, driver):
        self.driver = driver
        # self.link = Page.Locators.link

    def prompt_alert(self):
        time.sleep(2)
        alert = self.driver.switch_to.alert()
        alert.accept()

    def get_value(self, element):
        e = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, element)))
        m = e.text
        print(m)
        print("Dragan")
        return m

    def click_xpath(self, locator_of_element):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator_of_element)))

        e = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, locator_of_element)))
        e.click()

    def click_id(self, locator_of_element):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, locator_of_element)))

        e = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, locator_of_element)))
        e.click()

    ### Page need to be refreshed because drop down list does not work when import Florida and others
    def refresh_page(self):
        self.click_xpath(locator.refresh_one)
        self.click_xpath(locator.refresh_two)

    def import_place(self, place):

        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, locator.place)))
        e.send_keys(place)

    def check_need_to_click_next_month(self):

        self.click_id(locator.calendar)
        print("len is printing")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator.buttons_in_calendar)))

        el = self.driver.find_element(By.XPATH, locator.buttons_in_calendar)
        ls = el.find_elements(By.TAG_NAME, 'button')
        print(len(ls))
        for k in ls:
            print(k.text)
        if len(ls) < 2:  ###click on next month if enable days are not visible in the current month

            e = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//html/body/div[2]/div[1]/div/div/div/button[2]/svg')))
            e.click()

    def wait_new_window_or_tab(self):
        # Loop through until we find a new window handle
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        time.sleep(5)

    def message_to_cap(self):
        time.sleep(3)
        self.click_xpath(locator.contact_captain)
        time.sleep(5)
        """log in button"""
        self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/div[1]/h3/div/div/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "username").send_keys("dragan.dosen20@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div/div/div[2]/div/div[3]/form/button").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys("Atlantis123")
        time.sleep(1)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div/div/div/form/button").click()
        time.sleep(1)

    def cap_message(self):
        #### cap message ###
        time.sleep(3)
        self.click_xpath(locator.contact_captain)

        def is_element_visible():
            return self.driver.find_element(By.XPATH,
                                            locator.displayed).isDisplayed()

        flag = is_element_visible
        print(flag)

        if not flag:
            self.sign_up()
        else:
            self.login()

    def angler_choice(self):
        time.sleep(8)
        self.driver.find_elements(By.CLASS_NAME, 'listing-card-badges')
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, locator.angler_choice_label)))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, locator.angler_choice_label)))

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, locator.angler_choice)))

        angler_choice = self.driver.find_elements(By.CLASS_NAME, locator.angler_choice)
        desired_element = self.driver.find_elements(By.XPATH, locator.desired_element)

        for m in angler_choice:
            print(m.text)
            if (m.text == "Angler's choice"):
                m.click()
                print("click on angler")
                break
        print("desired has elements:")
        print(len(desired_element))
        print("will click on parrent")
        desired_element[0].click()
        print("clicked on parrent")

    def sign_up(self):
        print(" sign in method")
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[1]/h3/div/div/div/button")))
        e.click()
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='username']")))
        e.send_keys("dragan.dosen20@gmail.com")
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@]class='fbkr-button yellow']")))
        e.click()
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "password")))
        e.send_keys("Atlantis123")
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//html/body/div[8]/div[2]/div/div/div/div/form/button")))
        e.click()

    def adult_children(self):
        self.click_xpath(locator.adult_children)

        plus_adults = self.driver.find_element(By.XPATH, locator.adults)
        plus_kids = self.driver.find_element(By.XPATH, locator.children)
        adults_number = self.driver.find_element(By.XPATH,

                                                 '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div/div[2]/div[3]/div/div['
                                                 '2]/div[1]/div['
                                                 '2]/div/div/strong').text
        kids_number = self.driver.find_element(By.XPATH,

                                               '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div['
                                               '2]/div/div/strong').text
        print("broj odraslih i dece je:")
        print(adults_number)
        print(kids_number)
        while (adults_number != "4"):
            plus_adults.click()
            adults_number = self.driver.find_element(By.XPATH,

                                                     '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div['
                                                     '2]/div/div/strong').text
        while (kids_number != "2"):
            plus_kids.click()
            kids_number = self.driver.find_element(By.XPATH,

                                                   '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div['
                                                   '2]/div/div/strong').text

        # //*[@id="adults-plus"]
        # print(len(a))

    def filtering(self):
        time.sleep(2)
        original_window = self.driver.current_window_handle
        self.driver.find_element(By.LINK_TEXT, locator.check_availability).click()
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        time.sleep(15)
        # *[@id = "header-popover-container"]

        #self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/ul/li[3]/a").click()
        self.click_xpath(locator.result_container)
        print("clicked Filters")
        time.sleep(3)

        scrollElement = self.driver.find_element(By.XPATH, locator.scroll)
        scrollElement.send_keys(Keys.PAGE_DOWN)

        # 4.5
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "4_50")))
        e = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, locator.locator_45)))
        a = ActionChains(self.driver)
        a.move_to_element(e).perform()
        time.sleep(3)
        e.click()

        # inshore fishing
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.NAME, "fishing_type_inshore")))
        e = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, locator.locator_inshore)))
        a = ActionChains(self.driver)
        a.move_to_element(e).perform()
        time.sleep(1)
        e.click()
        scrollElement.send_keys(Keys.PAGE_DOWN)
        scrollElement.send_keys(Keys.PAGE_DOWN)

        time.sleep(5)
        #########   red sniper  ##############

        e = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                #(By.XPATH, "//html/body/div[5]/div[2]/div/div[1]/div[10]/div/div/div[10]/div/label")))
                (By.XPATH, locator.locator_red_sniper)))

        time.sleep(5)
        e.click()
        time.sleep(2)
        ##################################################

        ####button for filtering
        self.click_xpath(locator.btn_filtering)

        time.sleep(2)
        # Store the ID of the original window
        original_window = self.driver.current_window_handle
        wait = WebDriverWait(self.driver, 20)
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

    def is_element_visible(self):
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[1]/h3/div"))).isDisplayed()
        return e

    def login(self):
        print(" login method")

        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, locator.username_locator)))
        e.send_keys(testdata.user)
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "password")))
        e.send_keys(testdata.pass_value)
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "first-name")))
        e.send_keys("first-name")
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "last-name")))
        e.send_keys("last-name")

        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[2]/div/div[3]/form/button")))
        e.click()

        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[1]/h3/div/div/div/button")))
        e.click()
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='username']")))
        e.send_keys("dragan.dosen20@gmail.com")
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "///html/body/div[8]/div[2]/div/div/div/div[2]/div/div[3]/form/button")))
        e.click()
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "password")))
        e.send_keys("Atlantis123")
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div/form/button")))
        e.click()

    def message(self):

        ### group ###
        time.sleep(2)
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "cf-group-size")))
        e.click()
        time.sleep(2)
        el = self.driver.find_element(By.ID, "cf-group-size")
        ls = self.driver.find_elements(By.XPATH, "//*[@id='cf-group-size']/option")
        print(len(ls))
        ls[5].click()
        time.sleep(2)

        ###calendar###

        calendar = self.driver.find_element(By.ID, "cf-trip-date")
        calendar.click()
        ###I am was not able to solve problem with selecting enabled dates in that method
        ### but 18 sept is selected with code
        stores_table = self.driver.find_elements(By.XPATH, "//div[@class ='rdtDays']/table/tbody/tr/td")
        print(len(stores_table))
        stores_table.reverse()
        stores_table[18].click()
        """for m in storesTable:
            s = str(m)
            if 'rdtDay rdtNew' not in s:
                m.click()
                break"""
        time.sleep(2)

        ### trip drop down ###
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "cf-packages")))
        e.click()
        store_trip = self.driver.find_elements(By.XPATH, "//*[@id='cf-packages']/option")
        store_trip.reverse()
        store_trip[1].click()

        ### writing message ###
        e = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "contact-textarea")))
        e.send_keys("hello I am writing test message.")
        ### writing message is disabled as clicking on button for send message is disabled!!!

    def click_first_enabled_day(self):

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator.buttons_in_calendar)))
        el = self.driver.find_element(By.XPATH, '//html/body/div[2]/div[1]/div')
        a = el.find_elements(By.TAG_NAME,
                             'button')
        print("sada duzina se stampa")
        print(len(a))
        if len(a) == 0:  ###click on next month if enable days are not visible in the current month
            self.driver.find_element(By.XPATH,
                                     '//html/body/div[2]/div[1]/div/div/div/button[2]/svg').click()
        enabled_days = []
        for e in a:
            if e.is_enabled():
                print("enable")
                print(e.text)
                enabled_days.append(e)
            else:
                print("not enable")
                print(e.text)

        minimum = 10

        enabled_days[1].click()

    def return_drv(self):
        return self.driver
