#1: ValueError
#2: Done
#3: "Need to input an integer!"
#4. Try Block is checking if the input can be converted into the string, if not then it just continues indefinetly running
def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()