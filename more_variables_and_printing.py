store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

# f-string formatting
print(f"At {store} I bought some {item}.")

# Concatenation formatting
print("They sold for $" + str(price) + " each.")

# "dot format" formatting
print("I wanted to purchase {} of them.".format(quantity))

# Describing subtotal and tax amounts
print(f"The subtotal was ${subtotal:.2f}.")
print(f"The tax was ${tax:.2f}.")

# f-string formatting (corrected)
print(f"The total price, with tax included, was ${total:.2f}.")