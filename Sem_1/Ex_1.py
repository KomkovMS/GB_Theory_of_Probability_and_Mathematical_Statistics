"""
Из колоды, состоящей из 36 карт, случайным образом выбраны 5.
Сколькими способами можно выбрать эти карты так, чтобы  среди них оказалось
2 туза?

"""
import math


def func(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


# 1) Берем подмножество тузов:
combination_of_2_aces = func(4, 2)
print(combination_of_2_aces)  # 6  сочетаний из 2 тузов

a_subset_without_ace = func(32, 3)
print(a_subset_without_ace)  # 4960 cочетаний из 3 не тузов

c = a_subset_without_ace * combination_of_2_aces
print(c)  # 29 760 сочетаний из 5 карт, где 2 туза
