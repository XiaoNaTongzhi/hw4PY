# # Вычислить число c заданной точностью d

# # С семиара (pi)

# from math import pi

# d = input()
# accur = len(d)
# print(str(pi)[0:accur])


# # То же через округление 

# n = float(input('Введи десятичную дробь: '))
# d = float(input('Точность округления: ')) # или это - в число, или единицу - в строку
# if d == 1:
#     accur = 0
# else:
#     accur = len(d) - 2
# print(round(n, accur))



# # С проверкой ввода

# print('Введи десятичную дробь: ')
# n = float(input())
# print('Точность округления: ')
# d_str = input()

# # !!ВОПРОС!!
                                        # # Вот здесь как в разные переменные записать? 
                                        # # Он просто так не присваивает. (С записью в строку см. ниже).
# left, right = d_str.split(',')
# if right[-1] == 1:  
#     d = len(right)
# elif left == 1:
#     d = 0 
# else:
#    print('Точность указана неверно.')

# res = round(n, d)
# print('Ваш результат: ', res)



# # С проверкой ввода(строки)

# print('Введи десятичную дробь: ')
# n = float(input())
# print('Точность округления: ')
# dev_str = input().split(',')

# if dev_str[1][-1] == 1:                  # !! Не пойму, что тут не так
#     d = len(dev_str[1])
# elif dev_str[0] == 1:
#     d = 0 
# else:
#    print('Точность указана неверно.')

# res = round(n, d)
# print('Ваш результат: ', res)





# # Задайте натуральное число N.
# # Список простых множителей числа N.

# n = int(input('Введи число: '))
# if n == 1:
#     print(1)
# some_list = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if n % j == 0:
#                 break
#         else: 
#             some_list.append(i)
# print(*some_list, sep=', ')

  
  
  
# # Задайте последовательность чисел. 
# # Список неповторяющихся элементов исходной последовательности.

# some_list = list(map(int, input().split()))
# for i in some_list:
#     if some_list.count(i) == 1:
#         print(i, end= ' ')


