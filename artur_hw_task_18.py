#Задание №18


def sum_symbol_codes(first, last):
  total_sum = 0
  for i in range(ord(first), ord(last)+1):
      total_sum += i
  return total_sum


print(sum_symbol_codes('x', 'y'))



