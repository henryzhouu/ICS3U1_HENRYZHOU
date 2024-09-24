print("Enter the following information about an item you wish to purchase")
print()

name = input(("Enter Name of the item: "))
price = float(input("The price: $"))
quantity = int(input("How many do you want?"))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

#1)One was spread within 2 lines and one was put into just one line
#3)a prompt is a question: switching the order causes an issue because you aren't taking any input, 
    #but instead printing after it asks
#4) int stores it as a number, float stores it as a decimal number, without this it would store a string and not work