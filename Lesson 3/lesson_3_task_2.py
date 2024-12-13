from smartphone import Smartphone

catalog = []

try:
    catalog.append(Smartphone("Samsung", "Galaxy S23", "+79123456789"))
    catalog.append(Smartphone("Apple", "iPhone 14", "+79876543210"))
    catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79987654321"))


    for phone in catalog:
        print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

except ValueError as e:
    print(f"Ошибка при создании объекта Smartphone: {e}")