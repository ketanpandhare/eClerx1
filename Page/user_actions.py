from selenium import webdriver
from selenium.webdriver.common.by import By
from Page.input_parameters import Input_parameters
import re
import time


from Test.write_to_excel import Excel_operation

class User_actions():
    parameters = Input_parameters()
    def borwse_website(self,driver):
        driver.get(self.parameters.Website)


    def search_destinaion(self, driver):
        hotel_destination_element = driver.find_element(By.ID, 'hotels-destination')
        hotel_destination_element.send_keys(self.parameters.Destination)
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[contains(@class,'hotel-searchbox-drop-result-list')]/div[1]").click()

    def select_date(self,driver):
        check_in_calander = driver.find_element(By.XPATH,
                                                "//div[contains(@class,'time-tab checkin')]//input[contains(@class,'focus-input show-hightlight')]")
        check_in_calander.click()
        l_calender = driver.find_element(By.XPATH, "//div[@class='c-calendar-month'][1]//h3").text
        p = re.compile("\d+")
        l_calender_year = int(p.findall(l_calender)[0])

        p = re.compile("\w+")
        l_calender_month = p.findall(l_calender)[0]

        x = str("//div[contains(@class,'c-calendar__body')]//div[1]//li[text()='" + str(self.parameters.get_day()) + "']")
        while True:
            if self.parameters.get_year() == l_calender_year:
                if self.parameters.get_month() == l_calender_month:
                    from_date = driver.find_element(By.XPATH, x)
                    from_date.click()
                    to_date, flg = self.parameters.get_to_date()
                    if flg == 1:
                        x = str(
                            "//div[contains(@class,'mc-srh-box__forms')]//div[2]//div[1]//li[text()='" + str(
                                to_date) + "']")
                        driver.find_element(By.XPATH, x).click()
                    else:
                        x = str("//div[contains(@class,'c-calendar__body')]//div[1]//li[text()='" + str(to_date) + "']")
                        driver.find_element(By.XPATH, x).click()

                    break
                else:
                    driver.find_element(By.XPATH, "//span[contains(@class,'c-calendar-icon-next')]").click()
                    l_calender = driver.find_element(By.XPATH, "//div[@class='c-calendar-month'][1]//h3").text
                    p = re.compile("\d+")
                    l_calender_year = int(p.findall(l_calender)[0])

                    p = re.compile("\w+")
                    l_calender_month = p.findall(l_calender)[0]
            else:
                driver.find_element(By.XPATH, "//span[contains(@class,'c-calendar-icon-next')]").click()
                l_calender = driver.find_element(By.XPATH, "//div[@class='c-calendar-month'][1]//h3").text
                p = re.compile("\d+")
                l_calender_year = int(p.findall(l_calender)[0])

    def select_rooms(self,driver):
        # Select rooms and Guest
        ##driver.find_element(By.XPATH, "//p[@class='info show-hightlight']").click()
        rooms = driver.find_element(By.XPATH, "//div[@class='room-guest-container']//div[1]//div[1]//span[2]").text
        while True:
            if int(rooms) == self.parameters.Rooms:
                break
            else:
                driver.find_element(By.XPATH,
                                    "//div[@class='child-kid'][1]//i[@class='smarticon u-icon-ic_plus btn']").click()
                rooms = int(
                    driver.find_element(By.XPATH, "//div[@class='room-guest-container']//div[1]//div[1]//span[2]").text)

    def select_adults(self,driver):
        adults = int(driver.find_element(By.XPATH, "//div[@class='mc-srh-box__forms']//div[2]//div[1]//span[2]").text)
        while True:
            if adults == self.parameters.Adult:
                break
            else:
                driver.find_element(By.XPATH,
                                    "//div[@class='child-kid'][2]//i[@class='smarticon u-icon-ic_plus btn']").click()
                adults = int(
                    driver.find_element(By.XPATH, "//div[@class='mc-srh-box__forms']//div[2]//div[1]//span[2]").text)

    def select_children(self, driver):
        children = int(driver.find_element(By.XPATH, "//div[@class='choice']//div[3]//div[1]//span[2]").text)
        while True:
            if children == self.parameters.Children:
                break
            else:
                driver.find_element(By.XPATH,
                                    "//div[@class='child-kid'][3]//i[@class='smarticon u-icon-ic_plus btn']").click()
                children = int(driver.find_element(By.XPATH, "//div[@class='choice']//div[3]//div[1]//span[2]").text)
        driver.find_element(By.XPATH, "//span[contains(text(),'Done')]").click()

    def click_on_search_button(self, driver):
        driver.find_element(By.XPATH, "//i[@class='smarticon u-icon-ic_new_search_line icon-search']").click()
