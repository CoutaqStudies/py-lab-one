import random
import math
MIN = 0
MAX = 100

n = random.randint(MIN, MAX)
closest_power_of_two = int(math.pow(2, math.ceil(math.log(n, 2)))) if n!=0 else int(math.pow(2, 0))

integers = list()
print(f"n is {n}, the closest power of 2 (upper bound) is {closest_power_of_two}")
for i in range(closest_power_of_two):
    integers.append(random.randint(MIN, MAX) if  i<n else 0)

print(integers)
