print("TWO QUESTIONS!")
print("Think of an object and I'll try to guess it!")

object = input("\n\n\nQuestion 1) \n Is it an animal, vegetable, or mineral? ")


if object == 'animal':
    size = input("\n\n\nQuestion 2) \n Is it bigger than a breadbox?")
    if size == 'yes':
        print("\nMy guess is that you are thinking of a moose")
    if size == 'no':
        print("\nMy guess is that you are thinking of a squirrel")

if object == 'vegetable':
    size = input("\n\n\nQuestion 2) \n Is it bigger than a breadbox?")
    if size == 'yes':
        print("\nMy guess is that you are thinking of a watermelon")
    if size == 'no':
        print("\nMy guess is that you are thinking of a carrot")

if object == 'mineral':
    size = input("\n\n\nQuestion 2) \n Is it bigger than a breadbox?")
    if size == 'yes':
        print("\nMy guess is that you are thinking of a camaro")
    if size == 'no':
        print("\nMy guess is that you are thinking of a paperclip")


