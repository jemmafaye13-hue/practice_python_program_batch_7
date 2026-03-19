# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

text = input("Enter text: ")
prefix = input("Enter prefix to check: ")

if text[:len(prefix)] == prefix:
    print("Result: True")
else:
    print("Result: False")