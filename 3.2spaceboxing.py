earth_weight = float(input("Please enter your current earth weight (in pounds): "))

print("\nI have information for the following planets:")
print("   1. Venus")
print("   2. Mars")
print("   3. Jupiter")
print("   4. Saturn")
print("   5. Uranus")
print("   6. Neptune")

planet_choice = int(input("\nWhich planet are you visiting? "))

if planet_choice == 1:
    new_weight = earth_weight * 0.78
    print(f"\nYour weight would be {round(new_weight)} pounds on Venus.")
elif planet_choice == 2:
    new_weight = earth_weight * 0.39
    print(f"\nYour weight would be {round(new_weight)} pounds on Mars.")
elif planet_choice == 3:
    new_weight = earth_weight * 2.65
    print(f"\nYour weight would be {round(new_weight)} pounds on Jupiter.")
elif planet_choice == 4:
    new_weight = earth_weight * 1.17
    print(f"\nYour weight would be {round(new_weight)} pounds on Saturn.")
elif planet_choice == 5:
    new_weight = earth_weight * 1.05
    print(f"\nYour weight would be {round(new_weight)} pounds on Uranus.")
elif planet_choice == 6:
    new_weight = earth_weight * 1.23
    print(f"\nYour weight would be {round(new_weight)} pounds on Neptune.")
else:
    print("Invalid planet choice.")