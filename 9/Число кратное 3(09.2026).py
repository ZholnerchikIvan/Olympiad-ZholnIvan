n = str(input())

if not n.isdigit():
    print('error')
    exit()

digits = list('0123456789')
editedn = list() # Измененная строка для проверки на делимость
editednstr = str()
#digitIndx = 0 # Индекс числа из digits
integers = [] # Делимые на 3 числа


for i in range(len(n)):
    editedn = list(n)

    for b in range(len(digits)):
        editedn[i] = digits[b]
        print(f'Цифра {editedn[i]} на {digits[b]}')

        if editedn[i]  == digits[b]:
            continue

        if i == 0 and editedn[i] == 0:
            continue

        editednstr = "".join(editedn)

        if int(editednstr) % 3 == 0:
            integers.append(editednstr)


print(integers)