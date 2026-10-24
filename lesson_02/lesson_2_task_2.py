def is_year_leap(year):
    # Проверяем, делится ли год на 4 без остатка
    if year % 4 == 0:
        return True
    else:
        return False

# Вызываем функцию, передаем год и сохраняем результат в переменную
my_year = 2024  # Вы можете выбрать любой год
result = is_year_leap(my_year)

# Выводим результат в нужном формате
print(f"год {my_year}: {result}")