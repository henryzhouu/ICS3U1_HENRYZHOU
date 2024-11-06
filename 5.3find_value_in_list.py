import random
count = 0
ccount = 0
list = []

while count < 10:
    list.append(random.randrange(0,50))
    count += 1
print(list)

value = int(input("Value to Find: "))
while ccount < len(list):
    svalue = list[ccount]
    if svalue == value:
        print(f"The value {value} is in the list")
    ccount += 1