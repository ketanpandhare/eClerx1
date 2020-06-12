from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

from Page.input_parameters import Input_parameters
import time
from Test.write_to_excel import Excel_operation



class Extract_data():
    parameters = Input_parameters()

    def extract_hotels_data_and_write_to_excel(self, driver):
        # List down all hotels
        list1 = driver.find_elements(By.XPATH, "//div[@class='card-item-wrap']")
        write_obj = Excel_operation()
        write_obj.create_excel()
        parent_window = driver.current_window_handle
        for i in range(len(list1)):
            driver.delete_all_cookies()
            driver.find_elements(By.XPATH, "//div[@class='card-item-wrap']//div[@class='list-card-title ']//span[1]")[
                i].click()
            list_handle = driver.window_handles
            driver.switch_to_window(list_handle[1])
            #print(driver.current_url)
            #time.sleep(5)
            country = driver.find_element(By.XPATH, "//span[@class='detail-baseinfo_address']").text
            country = country.split(',')[-1]

            hotel_name = driver.find_element_by_tag_name("h1")
            hotel_name = hotel_name.text
            ratings = len(driver.find_elements(By.XPATH,
                                               "//div[contains(@class,'detail-baseinfo_base')]//i[@class='u-icon u-icon-diamond detail-baseinfo_title_level']"))
            room_list = driver.find_elements(By.XPATH, "//div[@class='roomname']")
            for l in range(len(room_list)):
                room_name = driver.find_elements(By.XPATH, "//div[@class='roomname']")[l].text
                j = l + 1
                x = str("(//div[@class='roomlist-container']//div[@class='roomlist-baseroom-card'])[" + str(
                    j) + "]//div[@class='salecard-bedfacility']/div[3]//span[starts-with(@class,'desc-text')]")
                y = str("(//div[@class='roomlist-container']//div[@class='roomlist-baseroom-card'])[" + str(
                    j) + "]//div[@class='note']")
                # print(x)
                # print(y)
                #driver.execute_script("window.scrollBy(0, 1000);")
                # time.sleep(3)
                try:
                    wait = WebDriverWait(driver, 10, poll_frequency=1,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
                    beds_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                 x)))
                except Exception:
                    print("Timeout:")
                beds_list = driver.find_elements(By.XPATH, x)
                for k in range(len(beds_list)):
                    beds_Amenities = driver.find_elements(By.XPATH, x)[k].text
                    after_tax = driver.find_elements(By.XPATH, y)[k].text
                    average_price = after_tax.split('$')[1]
                    data = list()
                    data.append(country)
                    data.append(self.parameters.Destination)
                    data.append(self.parameters.Check_in_date)
                    data.append(self.parameters.Night)
                    data.append(self.parameters.Adult)
                    data.append(hotel_name)
                    data.append(ratings)
                    data.append(room_name)
                    data.append(beds_Amenities)
                    data.append((average_price))

                    write_obj.append_to_execl(data)
                    #print("List_data", data)

            driver.close()
            driver.switch_to_window(parent_window)
            time.sleep(1)
            #print("=" * 10)

        time.sleep(2)
