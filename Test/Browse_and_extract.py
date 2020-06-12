from selenium import webdriver
from Page.Extract_data import Extract_data
import time
from Page.user_actions import User_actions


class BrowseAndExtract():
    def browse(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        action_obj=User_actions()
        extract_obj=Extract_data()

        #Users_action
        action_obj.borwse_website(driver)
        action_obj.search_destinaion(driver)
        action_obj.select_date(driver)
        action_obj.select_rooms(driver)
        action_obj.select_adults(driver)
        action_obj.select_children(driver)
        action_obj.click_on_search_button(driver)
        time.sleep(2)

        #Extract data and write to excel
        extract_obj.extract_hotels_data_and_write_to_excel(driver)
        print("*"*10)
        print("Done")
        print("*"*10)



b = BrowseAndExtract()
b.browse()
