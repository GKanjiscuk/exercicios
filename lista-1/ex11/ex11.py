import sys
sys.set_int_max_str_digits(0)

num = 2**1000000
carac = len(str(num))

print(f'2 elevado a um milhão possui {carac} caracteres')