'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''


def isprime(number):
    if number % 2 == 0:
        return False
    for dividor in range(3, int(number ** 0.5) + 1):
        if number % dividor == 0:
            return False
    return True


summ = 2
for number in range(3, 2000000, 2):
    if isprime(number):
        summ += number
print(summ)
