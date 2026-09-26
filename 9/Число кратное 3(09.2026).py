n = str(input())

if not n.isdigit():
    print('error')
    exit()

digits = '0123456789'
editedn = str() # Измененная строка для проверки на делимость
#digitIndx = 0 # Индекс числа из digits
integers = [] # Делимые на 3 числа


for i in range(len(n)):
    editedn = n

    for b in range(len(digits)):
        editedn = editedn[:i] + digits[b] + editedn[i+1:]

        print(f'Цифра {editedn[i]} на {digits[b]}')

        if int(editedn) % 3 == 0:
            integers.append(editedn)


print(integers)