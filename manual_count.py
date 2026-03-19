# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

text = input("Enter text: ")
target = input("Enter character/substring to count: ")
count = 0
n = len(target)

# Slide through the string checking for matches
for i in range(len(text) - n + 1):
    if text[i:i+n] == target:
        count += 1

print(f"Occurrences: {count}")