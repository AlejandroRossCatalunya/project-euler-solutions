'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

result = 2520
for dividor in range(11, 21):
    if result % dividor:
        gcd = dividor // 2
        while (result % gcd) or (dividor % gcd):
            gcd -= 1
        result *= dividor // gcd
print(result)
