import random
list = []
count = 0
for i in range(10):
    list.append(random.randint(0,100))

for i in range(len(list)):
    print(f"Slot {count} contains a {list[count]}")
    count += 1