a = input("Enter word: ").lower()
count = 0

for i in range(len(a)-1):
    substring = str(a[i] + a[i+1])
    if substring == "hi":
        count += 1
print(f"Hi appears {count} times")