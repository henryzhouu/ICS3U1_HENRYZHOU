number = int(input("Enter an integer: "))
total_sum = 0

for i in range(1, number + 1):
    print(i, end= "")
    total_sum += i


print(f"\nThe sum of numbers from 1 to {number} is {total_sum}.")
