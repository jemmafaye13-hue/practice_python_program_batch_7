# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

text = input("Enter text: ")
target = input("Enter character to find: ")
location = -1

# Iterate backwards to find the "last" occurrence first
for i in range(len(text) - 1, -1, -1):
    if text[i] == target:
        location = i
        break

if location != -1:
    print(f"Last index (rindex): {location}")
else:
    print("Not found")