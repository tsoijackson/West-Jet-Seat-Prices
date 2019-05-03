import sys
from seat_prices import WestJetWebScraper

if __name__ == "__main__":
    WestJetWebScraper().search_flight_prices(sys.argv[1], sys.argv[2], sys.argv[3])
