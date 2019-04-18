p = {}
for line in range(1, 31):
    p[line] = 1

# print(p)
check = 0
i = 1
j = 1
while i <= 31:
    if j == 15:
        break
    elif i == 31:
        i = 1
    else:
        check += 1
        if check == 9:
            p[i] = 0
            check = 0
            print("{}号下船了".format(i))
            j += 1
        else:
            i += 1
            continue
