firstmsg = input("Please input your first message:").lower()
secondmsg = input("Please input your second message: ").lower()

if firstmsg[-len(secondmsg):] == secondmsg:
    print("True")
else:
    print("False")