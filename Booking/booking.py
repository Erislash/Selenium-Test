from selenium import webdriver
from Booking.constants import *
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driverPath=CHROME_DRIVER_PATH, teardown=False ):
        self.driverPath = driverPath
        self.teardown = teardown

        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            print('Exiting...')
            self.quit()


    def landFirstPage(self):
        self.get(BASE_URL)


    def changeCurrency(self, currency="ARS"):
        buttons = self.find_elements(
            By.CSS_SELECTOR,
            '.bui-group__item button[data-tooltip-text]'
        )
        buttons[0].click()

        currencyBtn = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency={currency };top_currency=1"]'
        )
        currencyBtn.click()


    def changeLanguage(self, lang="es-ar"):
        buttons = self.find_elements(
            By.CSS_SELECTOR,
            '.bui-group__item button[data-tooltip-text]'
        )
        buttons[1].click()

        langBtn = self.find_element(
            By.CSS_SELECTOR,
            f'a[hreflang="{lang}"]'
        )
        langBtn.click()


    def selectPlaceToTravel(self, place="Córdoba, Argentina"):
        searchField = self.find_element(
            By.ID,
            'ss'
        )

        searchField.clear()
        searchField.send_keys(place)

        firstResult = self.find_element(
            By.CSS_SELECTOR,
            'ul[role="listbox"] li[data-i="0"]'
        )

        firstResult.click()

    def selectDates(self, checkInDate, checkOutDate):
        checkInElement = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{checkInDate}"]'
        )
        checkInElement.click()

        checkOutElement = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{checkOutDate}"]'
        )
        checkOutElement.click()


    def selectAccommodations(self):
        accommElement = self.find_element(
            By.ID,
            'xp__guests__toggle'
        )

        accommElement.click()
