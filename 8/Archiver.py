s = str(input())
K = str(None)
last = str()
csymbol = str()
col = int()
run = False

slist = list(s)
symbols = list()
cslist = list()

for i in range(len(slist)):
    if last is not None:
        if last != slist[i]:
            symbols.append(slist[i])
    else:
        symbols.append(slist[i])
    last = slist[i]

#print(symbols)

for i in range(len(symbols)):
    csymbol = symbols[i]

    for a in range(len(slist)):

        #print(f'a = {a}, len(slist) = {len(slist)}')

        if slist[a] == csymbol:
            col += 1
            run = True
            #print(f'Символ {csymbol}: {col}')
        elif run:
            if col > 1:
                cslist.append(str(col))
            cslist.append(csymbol)
            col = 0
            run = False
            break
        if a >= len(slist) - 1:
            if run:
                if col > 1:
                    cslist.append(str(col))
                cslist.append(csymbol)
                col = 0
                run = False
                break


K = ''.join(cslist)


print(K)
