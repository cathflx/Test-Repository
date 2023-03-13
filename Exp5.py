import time

def while_loop(n):
    number = 0
    i = 1
    while i <= n:
        number += i
        i += 1
    return number

def for_loop(n):
    start = 0
    for x in range (1, n+1):
        start += x
    return start 

n = 100000

time_start = time.time()

for_loop(n)

time_end = time.time()

time_total = time_end - time_start

print(time_total)
    