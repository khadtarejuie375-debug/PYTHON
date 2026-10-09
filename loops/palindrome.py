# Accept the name and check if its palindrome

name = input("enter name : ")

if name == name[::-1]:
  print("It is a palindrome")
else:
  print("Not a palindrome")


