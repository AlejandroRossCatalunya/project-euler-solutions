'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

number = 600851475143
dividor = 3
while number != 1:
    if number % dividor == 0:
        while number % dividor == 0:
            number //= dividor
    dividor += 2
print(dividor - 2)
