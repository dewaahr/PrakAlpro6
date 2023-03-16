def prima(n):
    list_prima = []
    for i in range(2,n):
        if i > 1:
            for j in range(2, int(i/2) + 1):
                if (i % j) == 0:
                    break
            else:
                list_prima.append(i)
    # print(list_prima)
    prima_terdekat = max(list_prima)
    print(f'Bilangan Prima Terdekat < {n} adalah {prima_terdekat}')

prima(5)
