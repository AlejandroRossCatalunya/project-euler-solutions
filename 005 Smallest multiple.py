'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

result = 2520
for divisor in range(11, 21):
    if result % divisor:
        gcd = divisor // 2
        while (result % gcd) or (divisor % gcd):
            gcd -= 1
        result *= divisor // gcd
print(result)
