# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print(
    "Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"
)
print("Введите число журавликов которое сделали Петя и Сережа: ")

Pety = int(input())
Serega = Pety
Katy = (Pety + Serega) * 2

print("Петя сделал : ", Pety, "Катя сделала : ", Katy, "Сережа сделал : ", Serega)

print("Вместе они сделали : ", Pety + Serega + Katy)
