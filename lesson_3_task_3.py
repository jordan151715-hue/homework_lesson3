from address import Address
from mailing import Mailing

to_address = Address(
    "101000",
    "Пенза",
    "Ленина",
    "10",
    "25"
)

from_address = Address(
    "170000",
    "Саратов",
    "Проспект Столыпина",
    "15",
    "12"
)

mailing = Mailing(
    to_address,
    from_address,
    559,
    "TRK123456789"
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
