#1. Yes they do
#2. Herons formula with functions has 32, Herons formula with functons has 42
#3. Much faster to do it in the one with functions because I only need to change one command, rather than 5


# --------- herons_formula.py----------------#
# import math


# def main():
#     area = triangle_area(3, 3, 3)
#     print(f"A triangle with sides 3, 3, 3 has an area of {area}")

#     area = triangle_area(3, 4, 5)
#     print(f"A triangle with sides 3, 4, 5 has an area of {area}")

#     area = triangle_area(7, 8, 9)
#     print(f"A triangle with sides 7, 8, 9 has an area of {area}")

#     area = triangle_area(5, 12, 13)
#     print(f"A triangle with sides 5, 12, 13 has an area of {area}")

#     area = triangle_area(10, 9, 11)
#     print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
#     area = triangle_area(8, 15, 17)
#     print(f"A triangle with sides 8, 15, 17 has an area of {area}")

#     area = triangle_area(9,9,9)
#     print(f"A triangle with sides 9, 9, 9 has an area of {area})
#     added this

# def triangle_area(a: int, b: int, c: int) -> float:
#     """Calculates a triangles area.
    
#     Args:
#         a: length of side a
#         b: length of side b
#         c: length of side c
    
#     Returns:
#         The area of the triangle
#     """
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     return area
#     # ^ after computing the area, "return" it


# if __name__ == "__main__":
#     main()
#-------------herons_formula_no_function.py-------------#
# import math


# def main():
#     a = 3
#     b = 3
#     c = 3
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 3, 3, 3 has an area of {area}")

#     a = 3
#     b = 4
#     c = 5
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 3, 4, 5 has an area of {area}")

#     a = 7
#     b = 8
#     c = 9
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 7, 8, 9 has an area of {area}")

#     a = 5
#     b = 12
#     c = 13
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 5, 12, 13 has an area of {area}")

#     a = 10
#     b = 9
#     c = 11
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
#     a = 8
#     b = 15
#     c = 17
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 8, 15, 17 has an area of {area}")

#     a = 9 
#     b = 9
#     c = 9
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s-a) * (s-b) * (s-c))
#     print(f"A triangle with sides 8, 15, 17 has an area of {area}")
# added this


# if __name__ == "__main__":
#     main()