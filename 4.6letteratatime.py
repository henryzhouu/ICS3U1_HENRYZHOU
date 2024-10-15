message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

# Count vowels
vowels = 'aeiouAEIOU'
vowel_count = 0
for i in range(len(message)):
    if message[i] in vowels:
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")

# 1.	Output of range(7): It shows range(0, 7).
# 2.	Converting to List: list(range(7)) gives [0, 1, 2, 3, 4, 5, 6].
# 3.	For “Hello”: len("Hello") is 5, so range(len(message)) is range(5) which includes 0, 1, 2, 3, 4.
# 4.	Length of “box”: The length is 3, and the index of ‘x’ is 2.
