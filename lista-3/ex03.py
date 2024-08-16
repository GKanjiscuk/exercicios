# input('Digite algo:')
paisA = 80000
paisB = 200000
anos = 0
while (paisA <= paisB):
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    anos = anos + 1
print(f'Foram necessários {anos} anos')

# paisA = int(paisA)
# paisB = int(paisB)

# print(f'O país A possui: {paisA} habitantes')
# print(f'O país B possui {paisB} habitantes')