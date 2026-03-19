# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

text = input("Enter text: ")
end_index = len(text)

# Iterate backwards from the end
for i in range(len(text) - 1, -1, -1):
    if text[i] != " ":
        end_index = i + 1
        break

print(f"Output: '{text[:end_index]}'")