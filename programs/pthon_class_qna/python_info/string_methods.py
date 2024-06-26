import random

numbers = ["a", "b", "c"]

for i in range(len(numbers)):
    random_num = random.randint(0, len(numbers) - 1)
    print(numbers[random_num], end=" ")