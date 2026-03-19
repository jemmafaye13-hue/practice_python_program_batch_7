# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

text = input("Enter text: ")
target = input("Enter character to find: ")
location = -1

for i in range(len(text)):
    if text[i] == target:
        location = i
        break # Stop at the first match

if location != -1:
    print(f"First index: {location}")
else:
    print("Not found")