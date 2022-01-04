'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

number = 600851475143
divisor = 3
while number != 1:
    if number % divisor == 0:
        while number % divisor == 0:
            number //= divisor
    divisor += 2
print(divisor - 2)
