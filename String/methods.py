# 07 OCT 2026
# ------------------------------------------- String Functions -------------------------------------------
text = "   hello, IMCC  "
name = "jui"

# 1. strip
print("Remove spaces from both ends: ", text.strip())

# 2. upper
print("Upper case:", text.upper())

# 3. lower
print("Lower case: ", text.lower())

# 4. Capitalize first letter
print("Capitalize first letter: ", name.capitalize())

# 5. Title case (capitalize each word):
print(text.title())

# 6.count occurances of a letter
print("Letter a occurs", text.count("a"))

# 7. Find the position of a substring (-1 if not found)
print("Position of Prajakta in the text is: ", text.find("Prajakta"))

# 8. Replace a substring
print(text.replace("Prajakta", "Praju"))

# 9. Check if string starts or ends with certain substring
print(text.startswith("  hello"))
print(name.endswith("a"))

# 10. Split string into
print(text.split())

# 11.
words = ["Python", "is", "fun"]
print(" ".join(words))



