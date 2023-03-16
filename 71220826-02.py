def deret_1(n):
    for i in range(n, 0, -1):
        hasil = 1
        for j in range(i, 0, -1):
            hasil= hasil*j
        print(hasil, end=' ')
        for k in range(i, 0, -1):
            print(k, end=' ')
        print()

deret_1(6)