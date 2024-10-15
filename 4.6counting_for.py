# 	Changing n to another name doesn’t affect the loop, it’s just a label.
# 	The first two range arguments are start and stop points.
#	The third argument is the step size.
# 	range(7) gives 0 to 6; range(3, 9) gives 3 to 8.
# 	(0, 10)
# 	(2, 22, 2)
print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(0, 5, 1):
    print(f"{n}. {message}")
