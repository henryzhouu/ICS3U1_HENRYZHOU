import random
list = []
count = 0
for i in range(1000):
    list.append(random.randint(10, 99))

for i in range(len(list)):
    print(list[i], end="  ")