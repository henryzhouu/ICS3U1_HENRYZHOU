#1) n+1 counts the amount of times the message is printed and ends it at 5. When removed it is neverending.
#2) Done
#3) Done
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()

n = 0
while n < 10:
    print(f"{n * 10}. {message}")
    n += 1

# Printing from 0 to 10 by 1
print("From 0 to 10 by 1:")
for i in range(0, 11, 1):
    print(i)
print()

# Printing from 10 to 0 by 1
print("From 10 to 0 by 1:")
for i in range(10, -1, -1):
    print(i)
print()

# Printing from 491 to 586 by 5
print("From 491 to 586 by 5:")
for i in range(491, 587, 5):
    print(i)
print()

# Printing from 124 to 810 by 14
print("From 124 to 810 by 14:")
for i in range(124, 811, 14):
    print(i)
print()

# Printing from -233 to -113 by 4
print("From -233 to -113 by 4:")
for i in range(-233, -112, 4):
    print(i)
print()

# Printing from 215 to 300 by 5
print("From 215 to 300 by 5:")
for i in range(215, 301, 5):
    print(i)
print()

# Printing from -310 to -94 by 8
print("From -310 to -94 by 8:")
for i in range(-310, -93, 8):
    print(i)
print()