def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "зима"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    elif 3 <= month <= 5:
        return "весна"
    else:
        return "Нет такого месяца"

try:


    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
