msg = input("Input a string: ").lower()
catcount = 0
dogcount = 0
for i in range(len(msg)-2):
    substring= msg[i: i+3]
    if substring == "dog":
        catcount += 1
    elif substring == "cat":
        dogcount += 1
if catcount == dogcount:
    print("True")
else:
    print("False")