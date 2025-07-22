from smartphone import Smartphone
catalog = [
    Smartphone("Alcatel", "2055", "+79212525236"),
    Smartphone("Nokia", "3310", "+79112527536"),
    Smartphone("Sony", "255", "+79212654236"),
    Smartphone("Simens", "С35", "+79812500036"),
    Smartphone("Samsung", "V25", "+79214445236")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} - {smartphone.phone_number}")