from address import Address
from mailing import Mailing

to_address = Address("191124", "Санкт-Петербург", "Невский проспект", "50", "10")
from_address = Address("123456", "Москва", "Ленинский проспект", "100")

try:
    mailing = Mailing(to_address, from_address, 350.0, "RU1234567890")

    apartment_to = f"- {mailing.to_address.apartment}" if mailing.to_address.apartment else ""
    apartment_from = f"- {mailing.from_address.apartment}" if mailing.from_address.apartment else ""

    print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}{apartment_from} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house}{apartment_to}. Стоимость {mailing.cost} рублей.")

except TypeError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")