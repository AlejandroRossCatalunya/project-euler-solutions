'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

# using Eratosthenes sieve
limit = 2000000
sieve = [True] * (limit + 1)
primes = []
start = 2
end = int(limit ** 0.5)
while start <= end:
    if sieve[start] is True:
        primes.append(start)
        for i in range(start * start, limit + 1, start):
            sieve[i] = False
    start += 1
for i in range(end + 1, limit + 1):
    if sieve[i] is True:
        primes.append(i)
print(sum(primes))
