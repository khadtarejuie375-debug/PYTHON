#Take a sentence from the user, split it into words, and print the longest word
# Take input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Words:", words)
print("Longest word:", longest)