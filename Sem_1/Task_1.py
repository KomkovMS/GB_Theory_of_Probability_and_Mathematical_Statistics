"""
В партии 10 деталей. Среди них 3 бракованные. Какова вероятность, что среди
5 ,взятых на удачу, 4 хорошие детали?
"""

# P(4 хорошие из 5) = (C(7,4) * C(3,1)) / C(10,5) = (7! / (4! * 3!))
# * (3! / (1! * 2!)) / (10! / (5! * 5!))

# вычисляем числитель
import math

numerator = math.factorial(7) // (math.factorial(4) * math.factorial(3)) * \
            math.factorial(3) // (math.factorial(1) * math.factorial(2))

# вычисляем знаменатель
denominator = math.factorial(10) // (math.factorial(5) * math.factorial(5))

# вычисляем вероятность
probability = numerator / denominator

print(round(probability, 3))

# Ответ: вероятность получить ровно 4 хорошие детали при выборе 5 деталей из
# партии, содержащей 10 деталей (среди которых 3 бракованные), равна 0.416.
