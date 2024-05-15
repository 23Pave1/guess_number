# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.
numbers_generator = (number ** 2 for number in numbers if number % 3 == 0)

result = sum(numbers_generator)
    
# Распечатайте сумму квадратов.

print(result)
