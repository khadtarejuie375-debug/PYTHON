# create heterogenous list of numbers and names .split list from highest number

l = [1, 2, 3, 4, 'Prajakta', 'Nandini', 50, 'Asha', 'Samruddhi', 40, 30 ]
nums = [1,2,3,4,50,40,30]
highest_num = max(nums)
print("Highest num in the list: ",highest_num)
print(l[:l.index(highest_num)])   #split og list l.index(highest_num) finds the index of 50 in th og list. the index of 50 is 6.  so l[:6] prints all elements before index 6
print(l[l.index(highest_num)+1:])   #index(highest_num) gives 6. so 6 + 1 = 7 i.e. a[7:] it prints from index 7 to the end
