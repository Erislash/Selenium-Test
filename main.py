from Booking.booking import Booking

with Booking() as bot:
    bot.landFirstPage()
    # bot.changeCurrency('USD')
    # bot.changeLanguage('en-us')
    bot.selectPlaceToTravel('Rosario, Santa Fe, Argentina')
    bot.selectDates('2021-12-25', '2022-01-15')
    bot.selectAccommodations()