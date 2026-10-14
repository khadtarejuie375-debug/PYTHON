#read all lines from a file into a list .print the total number of lines and display the 2nd and 4th line.
# Creating a file and writing content
with open("lines.txt", "w") as f:
    f.write("Python\n")
    f.write("Java\n")
    f.write("C Programming\n")
    f.write("HTML\n")
    f.write("CSS\n")

# Read all lines
with open("lines.txt", "r") as f:
    lines = f.readlines()
# Display the result
print("Total lines:", len(lines))
print("Second line:", lines[1].strip())
print("Fourth line:", lines[3].strip())