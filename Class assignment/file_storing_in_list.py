# 4.	Read a file, split its content into words, and store them in a list.
# i.	Print the total number of words.
# ii.	Print all unique words.

with open("words.txt", "w") as f:   #Creating a file and writing content
    f.write("python java python c java html")

with open("words.txt", "r") as f:   #Read the file
    content = f.read()

words = content.split()             #Split content into words

print("Total words:", len(words))   #Count total words

unique_words = set(words)           #Find unique words
print("Unique words:", unique_words)
