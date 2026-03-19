# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

text = input("Enter text: ")
length = int(input("Enter total length: "))

# Add spaces to the front until length is met
while len(text) < length:
    text = " " + text

print(f"Output: '{text}'")