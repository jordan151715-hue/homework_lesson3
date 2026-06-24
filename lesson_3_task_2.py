from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17", "+79001112233"),
    Smartphone("Samsung", "Galaxy S26", "+79002223344"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79003334455"),
    Smartphone("Honor", "600 Lite", "+79004445566"),
    Smartphone("Huawei", "P60", "+79005556677")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
