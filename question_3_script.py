soma = 0
for n in range(1000): # as it is below 1000, I have to put 1000 away :))
    if n % 3 == 0 or n % 5 == 0:
        soma += n
print(soma)
