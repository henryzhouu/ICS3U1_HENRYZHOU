import math

def area_circle(radius: int) -> float:
    return 2*radius*math.pi
def area_rectangle(length: float, width: float) -> float:
    return length*width
def area_square(side: float) -> float:
    return side*side
def area_triangle(base: float, height: float) -> float:
    return base*height*0.5

def main():
    while True:
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Quit")
        choice = input("Which shape: ")

        if choice == "1":
            base = float(input("\nBase: "))
            height = float(input("Height: "))
            area = area_triangle(base, height)
            print(f"\nThe area is {area}.")

        elif choice == "2":
            length = float(input("\nLength: "))
            width = float(input("Width: "))
            area = area_rectangle(length, width)
            print(f"\nThe area is {area}.")

        elif choice == "3":
            side = float(input("\nSide length: "))
            area = area_square(side)
            print(f"\nThe area is {area}.")

        elif choice == "4":
            radius = float(input("\nRadius: "))
            area = area_circle(radius)
            print(f"\nThe area is {area:.4f}.")

        elif choice == "5":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    main()