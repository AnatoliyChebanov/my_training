number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number)
primes=[] #True
not_primes=[] # False
for i in range(2,16):
    for j in range(2,i):
        if i%j == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)
print(primes)
print(not_primes)