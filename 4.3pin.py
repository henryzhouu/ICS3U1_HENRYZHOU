# How is a while loop similar to an if statement?
# works like an if statement checking if the statement is true
# How is a while loop different from an if statement?
# The only difference is that the program runs indefinetly
# What would we have to change in our program if the PIN was stored as an integer rather than a string? For example if it was initialized as PIN = 12345.
#We would have to make the pin 
# Comment out the line entry = input(...) from inside the while loop. What happens? Why?
#The program asks you to print the digit pin once and never again because there is no command in the while loop asking for it
# (Uncomment the entry = input(...) before you turn in the assignment.)
pin = "7890"

print = ("Welcome to the Bank of Julio Hel Pro")
entry = input("\nENTER YOUR FOR DIGIT PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")