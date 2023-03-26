"""
Из колоды 36 карт случайным образом берут 5 карт.
Найти вероятность того, среди 5 карт будет 2 туза.


"""
import math

num_of_favorable = 29760  # Число благоприятствующих исходов
card = 5
total_card = 36


def func(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


total_number = func(total_card, card)  # "общее число исходов"
print(total_number)  # общее число исходов 376992


def func_p(a, b):
    return a / b


p = func_p(num_of_favorable, total_number)
print(round(p, 4))    # Р= 29760 / 376992 = 0,0789

# Ответ: вероятность взять 5 карт с 2 тузами  0,0789  или около 8%
