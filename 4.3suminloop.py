print("I will add up all the integers you give me")
sum = 0
n = 1
while True:
    number= int(input("number?"))
    sum += number
    if number == 0:
        break
    print(f"Sum so far is {sum}")
    n+=1
print(f"The total is {sum}")