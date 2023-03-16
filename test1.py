n=21
primes = []
for num in range(2,n):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
print(primes)



n=23

# for i in range(2,n):
#         if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#             print(i)
# # print(bil)
# # print(max(bil))
num=[]
for i in range(n):
    num.append(i)
print(num)
for i in num:
    
