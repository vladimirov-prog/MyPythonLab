# Условный оператор. Задача 3

num = int(input("Введите целое число: "))

if num > 0:
    num += 1
elif num < 0:
    num -= 2
else:
    num = 10

print(f"Полученное число: {num}")
