import random

list1 = [random.randint(1, 100) for _ in range(10)]

list2 = list1[:]

list1[-1] = -7

print("List 1:", " ".join(map(str, list1)))
print("List 2:", " ".join(map(str, list2)))