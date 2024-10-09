# # #Create a loop that counts from 0 to 10, but skip the number 7.
# # x = 0
# # while x <= 10:
# #     if x == 7:
# #         x += 1
# #         continue
# #     print(x)
# #     x += 1
# # total = 0
# # Create a loop that will add the numbers from 5 to 20 but not any multiples of 3. Use modulus.
# # for number in range(5, 21):
# #     if number % 3 != 0:
# #         total += number

# # print(f"The total is {total}")
# #Ask the user for a starting number and an ending number. The program will get the sum of all the numbers from the start to the end (using a loop). However, our program is a bit of a diva: the program will stop summing the numbers if it encounters a 13 or a 31. It will still output the sum up to that point.

# # start = int(input("Enter the starting number: "))
# # end = int(input("Enter the ending number: "))

# # total = 0

# # for number in range(start, end + 1):
# #     if number == 13 or number == 31:
# #         break
# #     total += number

# # print(f"The sum of numbers from {start} to {end}, stopping if 13 or 31 is encountered, is: {total}")

# Create an infinite loop using while True:. In that loop ask the user for a word. For each word they enter, output the following "Your word: {word}". If ever they enter the word "stop" the program will break out of the loop. Finally the program will output "Goodbye!".
# while True:
#     word = input("Enter a word: ")
#     if word == "stop":
#         break
#     print(f"Your word: {word}")
    
# print("Goodbye!")