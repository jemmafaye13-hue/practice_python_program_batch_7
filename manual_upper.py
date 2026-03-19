# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

text = input("Enter text: ")
result = ""

for char in text:
    if 'a' <= char <= 'z':
        # Shift ASCII value from lower to upper
        result += chr(ord(char) - 32)
    else:
        result += char

print("Output:", result)