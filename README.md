# West-Jet-Seat-Prices

![](example.gif)

### How to Run
* Install Python3
* Install required libraries: pip3
* Edit and correct chromedrive path to you computer
    * open seat_prices.py
    * edit and paste your chromedriver path global variable: CHROMEDRIVER_PATH
* Run program to find seat prices
    * Enter into console: python3 main.py DEPART_CODE ARRIVAL_CODE DATE(YYYY-MM-DD)
        * main.py has 3 arguements: flights departing city, arriving city, and date of flight
        * example input: python3 main.py SFO YVR 2019-05-20
    * Some pages may take 4 - 8 seconds to load in data before next browser automation step