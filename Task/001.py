# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# print("Введите число: ")
# num = float(input())
# sum_digits = 0
# num = num * (10 ** len(str(num)))
# if num < 0:
#     num = num * -1

# while num:
#     sum_digits = sum_digits + (num % 10)
#     num = num // 10

# print(int(sum_digits))


num = str(input("Введите число: ")).replace('.', '')
print(sum(list(map(int, num))))
