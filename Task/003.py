# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

# list = []
# result = 0
# num = int(input("Введите размер списка: "))
# if num <= 0:
#     print("Error")
# else:
#     for i in range(1, num + 1):
#         numbers = (round((1 + 1/i) ** i))
#         list.append(numbers)
#         result += numbers
#     print(list)
#     print(result)



num = int(input("Введите размер списка: "))
list = [round((1+1/i)**i) for i in range(1, num+1)]
print(f"{list} \nСумма: {round(sum(list))}")