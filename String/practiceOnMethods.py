#txt = "ha"
#print(txt * 3)

# accept your name and find out the occurances of letter a

name = input("enter name")
print("occurance count",name.count("a"))
print(name.replace("jui","aaa"))
print(name.split())
print(sorted(name))

#empty List
my_list = []
print(my_list)   #[]

#with items
fruits = ["apple" , "banana" , "cherry"]
print(fruits)

#to access any item from list we can use index
#positive indicate from start negative numbers indicate index from 
#0 is first element and -1 is last
num = [10,20,30]
print(num[0])
print(num[-2])

#append item in list
color = ["red","blue"]
color.append("green")
print("after adding at last",color)

#num.remove(0) #removes specified item
#num.pop() #removes last item

#Functions
#Length
numbers = [1,2,3,4,5,8,9]
print("no of items in list",len(numbers))

#sum
print("Sum of the list numbers is",sum(numbers))

#sorting
print("list in Ascending order",sorted(numbers))
print("list in Descending order",sorted(numbers,reverse=True))

#QUE -1.create a list of 10 numbers and display the sum of last 4 elements
#     2.remove the items from the list located at 2nd and 5th position
#     3.print the diff of highest and smallest number in the list
#     4.append a new element in the list which is half of the item located in the 3rd position 

list = [1,2,3,4,5,6,7,8,9,10]
#1.
print("sum of last 4 elements:" , sum(list[-4:]))
#2.
del list[2]
del list[4]
print("After removing:" , list)
#3.
print("Difference:", max(list) - min(list))
#4. 
list.append(list[2] / 2)
print("Final list:", list)