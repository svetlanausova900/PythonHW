n = int(input("Введите месяц от 1 до 12:"))
def month_to_season(n):
    if 1 <= n <= 2 or n == 12:
        return "Зима"
    elif 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"
print(month_to_season(n))