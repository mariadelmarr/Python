x = 0
y = 1
ficonacci = True

while ficonacci:
    print(y)
    t = y
    y = x + y
    x = t
    ficonacci = True if input ('Continuar? s/n ') == 's' else False
    