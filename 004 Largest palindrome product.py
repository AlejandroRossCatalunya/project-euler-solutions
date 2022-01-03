'''
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

max_palindrome = 0
for mul1 in range(999, 100, -1):
    for mul2 in range(999, 100, -1):
        number = mul1 * mul2
        if number == int(str(number)[::-1]) and number > max_palindrome:
            max_palindrome = number
print(max_palindrome)
