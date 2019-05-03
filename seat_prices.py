import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = "/Users/jacksontsoi/Github/West-Jet-Seat-Prices/chromedriver"

class WestJetWebScraper:

    def __init__(self):
        self.chromedriver_path = CHROMEDRIVER_PATH
        self.driver = webdriver.Chrome(self.chromedriver_path)

        self.title = 'Mr.'
        self.first_name = 'firstName'
        self.last_name = 'lastName'
        self.phone_number = '0000000000'
        self.email = 'email@gmail.com'
        self.birthdate_day = '5'
        self.birthdate_month = 'May'
        self.birthdate_year = '1990'

        self.page_1_wait = 1
        self.page_2_wait = 7
        self.page_3_wait = 8
        self.page_4_wait = 2

    def search_flight_prices(self, start: str, end: str, date: str):
        query = self.build_search_query(start, end, date)

        # Page 1
        self.open_webpage(query)
        self.select_economy_class()
        
        # Page 2
        self.click_continue_button()

        # Page 3
        self.click_skip_sign_in_button()
        self.fill_out_guest_details_form()
        
        # Page 4
        self.print_seat_prices()

    def open_webpage(self, url:str):
        self.driver.get(url)

    def select_economy_class(self):
        try:
            self.click_economy_view_button()
            self.click_economy_select_button()
        except:
            self.driver.quit()
            raise Exception("Webdriver could not find html element. Incorrect webpage due to incorrect parameters or element did not load in time. Double check if query could find an existing flight.")

    def click_economy_view_button(self):
        time.sleep(self.page_1_wait)
        self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[3]/div[2]/ul/li/div[2]/div[1]/ul/li[1]/button').click()

    def click_economy_select_button(self):
        self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[3]/div[2]/ul/li/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/button').click()

    def click_continue_button(self):
        time.sleep(self.page_2_wait)
        self.driver.find_element_by_xpath('//*[@id="summaryContinue"]').click()

    def click_skip_sign_in_button(self):
        time.sleep(self.page_3_wait)
        self.driver.find_element_by_xpath('//*[@id="btn-skip-sign-in"]').click()

    
    def fill_out_guest_details_form(self):
        self.select_title()
        self.fill_out_first_name()
        self.fill_out_last_name()
        self.select_birthdate()
        self.fill_out_phone_number()
        self.fill_out_email()
        self.click_guest_details_form_continue_button()

    def select_title(self):
        Select(self.driver.find_element_by_xpath('//*[@id="adult-1-title"]')).select_by_visible_text(self.title)

    def fill_out_first_name(self):
        self.driver.find_element_by_xpath('//*[@id="adult-1-firstName"]').send_keys(self.first_name)

    def fill_out_last_name(self):
        self.driver.find_element_by_xpath('//*[@id="adult-1-lastName"]').send_keys(self.last_name)

    def select_birthdate(self):
        Select(self.driver.find_element_by_xpath('//*[@id="adult-1-day"]')).select_by_visible_text(self.birthdate_day) # Day
        Select(self.driver.find_element_by_xpath('//*[@id="adult-1-month"]')).select_by_visible_text(self.birthdate_month) # Month
        Select(self.driver.find_element_by_xpath('//*[@id="adult-1-year"]')).select_by_visible_text(self.birthdate_year) # Year

    def fill_out_phone_number(self):
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone_number)

    def fill_out_email(self):
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.email)

    def click_guest_details_form_continue_button(self):
        self.driver.find_element_by_xpath('//*[@id="continue"]').click()
    
    def print_seat_prices(self):
        time.sleep(self.page_4_wait)

        # Select all html divs representing a seat
        seats = self.driver.find_elements_by_xpath('//*[@id="bookingSeatMapPage"]/seat-map/div[2]/div[2]/div[2]/plane/div/div[1]/div/*/*')
        for seat in seats:
            if seat.get_attribute('data-seatnum') != None:

                price = "None"
                if len(seat.text) > 0:
                    price = seat.text

                print("Seat:", seat.get_attribute('data-seatnum'), "; Price:", price)


    def validate_date_correct_format(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except:
            self.driver.quit()
            raise Exception("Incorrect data format, should be YYYY-MM-DD")

    def build_search_query(self, start: str, end: str, date: str):
        self.validate_date_correct_format(date)
        return "https://www.westjet.com/shop/?lang=en&type=search&origin={}&destination={}&adults=1&children=0&infants=0&outboundDate={}&returnDate=&companionvoucher=false&iswestjetdollars=false&promo=&currency=USD".format(start, end, date)


if __name__ == "__main__":
    # WestJetWebScrapper().search_flight_prices('SNA', 'YVR', 'date')
    # WestJetWebScrapper().search_flight_prices('SNA', 'YVR', '2019-05-07')
    pass
