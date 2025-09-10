year = int(input("Введите год:"))
def is_year_leap(year):
        if year % 4 == 0:
            return (f"Год {year}: true")
        else:
            return (f"Год {year}: false")
answer = is_year_leap(year)
print(answer)