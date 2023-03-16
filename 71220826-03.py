def deret_tinggilebar(tinggi,lebar):
    for i in range(1, tinggi*lebar+1):
        print(i, end=" ")
        if i % lebar == 0:
            print()

deret_tinggilebar(5,6)