'''
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def collatz_sequence(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n // 2


seq = {2: 2, 4: 3, 5: 6, 8: 4, 10: 7, 13: 10, 16: 5, 20: 8, 40: 9}
for number in range(3, 1000000):
    if number not in seq.keys():
        current = [number]
        new_number = collatz_sequence(number)
        while new_number not in seq.keys():
            current.append(new_number)
            new_number = collatz_sequence(new_number)
        count = seq[new_number]
        for new_number in current[::-1]:
            count += 1
            seq[new_number] = count
max_freq = 0
for key, value in seq.items():
    if value > max_freq:
        max_freq = value
        number = key
print(number)
