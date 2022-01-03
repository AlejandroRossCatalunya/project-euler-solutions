'''
Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''

sum1, sum2 = 0, 0
for number in range(1, 101):
    sum1 += number**2
    sum2 += number
print(sum2**2 - sum1)
