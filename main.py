# УПРАЖНЕНИЕ 1. Функции lambda и map
# arr = list(map(int, input().split()))
# print(arr)
# res = list(map(lambda x: x**2, arr))
# print(res)
###################################################################################################################################

# УПРАЖНЕНИЕ 2. Функция filter
# def f1(n):
#     return n%2==0
# pre_arr = input().split()
# print(pre_arr)
# pre_arr = list(map(int, pre_arr))
# arr = list(filter(f1, pre_arr))
# print(arr)
###################################################################################################################################

# УПРАЖНЕНИЕ 3. Функция zip
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [11, 22, 33, 44, 55]
# arr3 = list(zip(arr1, arr2))
# print(arr3)
###################################################################################################################################

# УПРАЖНЕНИЕ 4. Функция enumerate
# arr = [11, 22, 33, 44, 55]
# res = list(enumerate(arr))
# print(res)
###################################################################################################################################

# ЗАДАЧА 1. Дан список [3, "afg", 555, 67, "csv", "txt", "com", 98, 0, "jocker"]. Вывести все цифоы в один список, а все буквы -
# в другой, используя функцию filter.       (45:19)
# def fNum(argument):
#     return str(type(argument)) == "<class 'int'>"

# def fWord(argument):
#     return str(type(argument)) == "<class 'str'>"

# arr = [3, "afg", 555, 67, "csv", "txt", "com", 98, 0, "jocker"]
# resNum = list(filter(fNum, arr))
# resWord = list(filter(fWord, arr))
# print(resNum)
# print(resWord)
###################################################################################################################################

# ЗАДАЧА 2. Дано вещественное число. Показать сумму составляющих его чисел.
# Мой вариант 1:
# def Poryadok(value):
#     poryadok = 0
#     while (value > 0):
#         poryadok = poryadok + 1
#         value = int(value / 10)
#     return poryadok

# def Dif(value):
#     res = []
#     por = Poryadok(value)
#     for i in range (1, por+1):
#         res.append(int(value / (10**(por-i))))
#         value = value - res[i-1]*(10**(por-i))
#     return res

# def Sum(array):
#     sum = 0
#     for i in range(0, len(array)):
#         sum = sum + array[i]
#     return sum

# value = 10001567
# arr = Dif(value)
# res = Sum(arr)
# print(res)

# Вариант из занятия:
# value = 1000156.7
# print(sum(map(lambda x: int(x), str(value).replace(".", ""))))

# К сведению:
# print(sum(map(lambda x: int(x), "12345"))) # Воспринимает строку как последовательность символов и пробегается по каждому символу.
# 1:23:20
###################################################################################################################################

# ЗАДАЧА 3. Дан список целых чисел. Оставить в нем только двузначные числа.
# data = [2, 73, 8, 91, 90, 5, 3, 12, 11, 7, 4, 34]
# print(data)
# res = list(filter(lambda x: x / 10 >= 1, data))
# print(res)
