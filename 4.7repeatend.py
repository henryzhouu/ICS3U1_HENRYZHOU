msg = input("Please print your message: ")
num = int(input("Please input the number: "))
response = ''
lastchar = msg[-num:]
for i in range (num):
    response += lastchar
print(response)