import random
random_set = {random.randint(15, 45) for _ in range(10)}
print("Original Set:", random_set)

less_than_30_count = sum(1 for num in random_set if num < 30)
print("Numbers less than 30:", less_than_30_count)

filtered_set = {num for num in random_set if num <= 35}
print("Filtered Set (<=35):", filtered_set)
