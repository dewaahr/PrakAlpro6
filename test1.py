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



