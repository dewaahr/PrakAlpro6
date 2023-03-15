
# 2
n=3
for i in range(n, 0, -1):
    result = 1
    for j in range(i, 0, -1):
        result *= j
    print(result, end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

# 3

# tinggi=5
# lebar=4
# n=tinggi*lebar
# for i in range(1,n//lebar):
#     print(i,end=' ')
#     for i in range(1,n//lebar):

tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

for i in range(1, tinggi*lebar+1):
    print(i, end=" ")
    if i % lebar == 0:
        print()
