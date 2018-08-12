# Find the element that appears once
#Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
#Output: 2

arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
#arr = [1, 3, 3, 4, 5, 1, 5]
#arr = [2, 3, 3, 2, 1]
#arr = [1, 2, 2, 1, 3]
count = 0
temp = 0
arr.sort()
print(arr)
for i in range(len(arr)-1):
	#print(i)

	#Check if the first element
	if arr[0] is not arr[1] and len(arr) > 1:
		temp = arr[0]
		break

	if arr[i] is arr[i + 1]:
		temp = 0
	else:
		# Check if the last element
		if i is len(arr) - 2:
			temp = arr[i + 1]
			break

		temp = arr[i]

	if temp is not 0:
		count = count + 1
	else:
		count = 0

	if count > 1:
		break

print(temp)
