"""
На 5 одинаковых карточках написаны буквы Ч, А, Й ,К, И
Какова вероятность, что получится слова ЧАЙКИ
"""

# Вероятность того, что буква Ч будет первой в слове, равна 1/5, потому что
# на каждой карточке находится одна из пяти букв и вероятность выбора буквы Ч
# из них равна 1/5.
#
# После выбора буквы Ч, вероятность выбора буквы А из оставшихся четырех
# карточек равна 1/4, потому что одна карточка с буквой Ч уже выбрана.
#
# Далее, вероятность выбора буквы Й из оставшихся трех карточек равна 1/3,
# а вероятность выбора буквы К из оставшихся двух карточек равна 1/2.
#
# Наконец, вероятность выбора последней буквы И из оставшейся одной карточки
# равна 1/1.
#
# Поэтому, общая вероятность того, что мы получим слово ЧАЙКИ, равна
# произведению всех вероятностей:
#
# 1/5 * 1/4 * 1/3 * 1/2 * 1/1 = 1/120
#
# Таким образом, вероятность получить слово ЧАЙКИ равна 1/120.


cards = ['Ч', 'А', 'Й', 'К', 'И']  # список букв на карточках
word = 'ЧАЙКИ'  # заданное слово
prob = 1  # инициализируем вероятность

# проходим по буквам слова и вычисляем вероятность
for letter in word:
    count = cards.count(letter)  # считаем, сколько карточек осталось с этой
    # буквой
    prob *= 1 / count  # делим 1 на это количество и умножаем на вероятность

print("Вероятность получить слово 'ЧАЙКИ' равна", float(prob)) # 0.0083333
