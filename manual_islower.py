# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

text = input("Enter text: ")
all_lower = True

for char in text:
    # If we find any uppercase letter, it's False
    if 'A' <= char <= 'Z':
        all_lower = False
        break

print("Is all lower?", all_lower)