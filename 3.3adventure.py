print("WELCOME TO MITCHELL'S TINY ADVENTURE!")

act1 = input('\nYou are in a creepy house! Would you like to go "upstairs" or into the "kitchen"? ')

if act1 == "kitchen":
    print("\nThere is a long countertop with dirty dishes everywhere. Off to one side, there is, as you'd expect, a refrigerator.")
    act2 = input('You may open the "refrigerator" or look in a "cabinet": ')
    
    if act2 == "refrigerator":
        print("\nInside the refrigerator you see food and stuff. It looks pretty nasty.")
        act3 = input('Would you like to eat some of the food? ("yes" or "no"): ')
        
        if act3 == "yes":
            print("\nYou eat the food and get food poisoning. You die. THE END.")
        elif act3 == "no":
            print("\nYou decide not to eat and die of starvation... eventually. THE END.")
    
    elif act2 == "cabinet":
        print("\nYou find a stack of plates and a rusty knife.")
        act3 = input('Would you like to take the "knife" or leave it? ("yes" or "no"): ')
        
        if act3 == "yes":
            print("\nYou take the knife, but it’s cursed! You vanish into thin air. THE END.")
        elif act3 == "no":
            print("\nYou leave the knife, but you hear something creeping behind you... You are never seen again. THE END.")

elif act1 == "upstairs":
    print("\nUpstairs you see a hallway. At the end of the hallway is the master bedroom. There is also a bathroom off the hallway.")
    act2 = input('Would you like to enter the "bedroom" or the "bathroom"?: ')
    
    if act2 == "bedroom":
        print("\nYou are in a plush bedroom with expensive-looking hardwood furniture. The bed is unmade. In the back of the room, the closet door is ajar.")
        act3 = input('Would you like to open the closet door? ("yes" or "no"): ')
        
        if act3 == "yes":
            print("\nYou open the door and find a secret passage, leading you to safety. You escape! THE END.")
        elif act3 == "no":
            print("\nYou ignore the closet. Suddenly, the room grows cold, and you feel a presence behind you. You are never heard from again. THE END.")
    
    elif act2 == "bathroom":
        print("\nYou step into the bathroom. It's eerily quiet, and the mirror is foggy.")
        act3 = input('Would you like to wipe the "mirror" or leave the room? ("wipe" or "leave"): ')
        
        if act3 == "wipe":
            print("\nYou wipe the mirror, and a face appears behind you! You scream as you vanish into the mirror. THE END.")
        elif act3 == "leave":
            print("\nYou leave the bathroom and run downstairs. You manage to escape the house safely. THE END.")