# 7. Найти сумму десяти первых чисел ряда Фибоначчи.


fibonachi_1 = -1
fibonachi_2 = 1
num_fibonachi = 10
i = 0
fibonachi_sum = 0
while i < num_fibonachi + 1:
    fibonachi_n = fibonachi_1 + fibonachi_2
    fibonachi_1 = fibonachi_2
    fibonachi_2 = fibonachi_n
    i += 1
    fibonachi_sum += fibonachi_n
print('сумма первых', num_fibonachi, 'чисел Фибоначчи равна - ', fibonachi_sum)

