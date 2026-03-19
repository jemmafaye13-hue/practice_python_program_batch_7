# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

text = input("Enter text: ")
length = int(input("Enter total length: "))

# Same logic as rjust, but using '0'
while len(text) < length:
    text = "0" + text

print("Output:", text)