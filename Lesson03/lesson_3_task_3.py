from mailing import Mailing
from address import Address

to_address = Address("195255", "Moscow", "Lenina", 174, 25)
from_address = Address("190003", "Saint-Petersburg", "Kalinina", 18, 44)

mailing = Mailing(to_address, from_address, "12.75", "track15025")

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей.")