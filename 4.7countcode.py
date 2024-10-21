msg = input("Please input your string: ").lower()
count = 0
for i in range(len(msg)-1):
    if msg[i] == "c" and msg [i+1] == "o" and msg [i + 3] == "e":
        count += 1
print(count)