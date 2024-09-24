import math
print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
#the (-) symbol subtracts numbers
print(f"there are {33 - 11} boys.")
print()
#the (+) symbol divides numbers 
boys = round(33-11/33,2)
print(f"That means {girls} % are girls...")
print("and {} % are boys.".format(boys))
print()
print("If we made groups of six...")
#the (//) symbol is floor divison | finds the biggest number that will divide into the first number using the second number as another factor
print(f"There would be {33 // 6} groups of six.")
#the (%) symbol divides the number and then outputs the remainder
print(f"And then a smaller group of {33 % 6} people.")
#duplicates "-" 30 times and prints it out
print("-" * 30)
print("If we had 17 apples and 3 people...")
#Floor division again
print(f"Each person would get {17 // 3} whole apples.")
#the modulus (%) symbol divides the number and then outputs the remainder
print(f"There would be {17 % 3} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
#the (*) sign multiplies the 2 and the 5, outputting 10
print("they would each pay ${}.".format(2 * 5))