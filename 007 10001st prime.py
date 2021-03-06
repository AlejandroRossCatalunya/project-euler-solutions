'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''


def isprime(number):
    if number % 2 == 0:
        return False
    for dividor in range(3, int(number ** 0.5) + 1):
        if number % dividor == 0:
            return False
    return True


number, count = 13, 6
while count < 10001:
    number += 2
    if isprime(number):
        count += 1
print(number)
