#WAP to read a file and count how many vowels are present in its content .

# Creating a file and writing a content
with open("vowels.txt", "w") as f:
    f.write("Python is an easy programming language.")

# Read the file
with open("vowels.txt", "r") as f:
    content = f.read()

# Count vowels
vowels = "aeiouAEIOU"
count = 0

for i in content:
    if i in vowels:
        count += 1

print("File content:", content)
print("Total vowels:", count)
