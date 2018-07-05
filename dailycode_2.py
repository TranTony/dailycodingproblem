#Given an array of integers, return a new array such that each element 
#at index i of the new array is the product of all the numbers 
#in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], 
#the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].




#list = [1, 2, 3, 4, 5]
list = [3, 2, 1]
result = []

for i in range(len(list)):
	multi = 1;
	for j in range(0, i):
		multi *= list[j]
	for t in range(i+1, len(list)):
		multi *= list[t]
	result.append(multi)
		

print(result)