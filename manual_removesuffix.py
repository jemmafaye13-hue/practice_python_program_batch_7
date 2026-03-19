# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

text = input("Enter text: ")
suffix = input("Enter suffix to remove: ")

# Check if the end of text matches the suffix
if text[-len(suffix):] == suffix:
    print("Output:", text[:-len(suffix)])
else:
    print("Output:", text)