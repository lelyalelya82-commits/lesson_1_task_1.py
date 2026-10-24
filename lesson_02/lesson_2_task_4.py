def fizz_buzz(n):
    # Проходим циклом от 1 до n включительно
    for i in range(1, n + 1):
        # ВАЖНО: Проверку на 3 и 5 (то есть на 15) нужно делать ПЕРВОЙ,
        # иначе сработает условие только на 3 или только на 5.
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Вызов функции для проверки
fizz_buzz(15)