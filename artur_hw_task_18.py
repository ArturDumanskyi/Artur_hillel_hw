#Задание №18


def sum_symbol_codes(first, last):
  ord_1 = 0
  for i in range(ord(first), ord(last)+1):
      ord_1 += i
  return ord_1


print(sum_symbol_codes('x', 'y'))



