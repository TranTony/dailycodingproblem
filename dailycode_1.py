
#Good morning! Here's your coding interview problem for today.
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

K = 18
list = [11, 15, 3, 7]
count = 0
for i in range(len(list) - 1):
	for j in range(i+1,len(list)):
		if (K - list[i]) == list[j]:
			count+=1
			print(str(list[i]) + " and " + str(list[j]))

print("There are "  + str(count) + " pairs")


def interleave(list):
  queue = []
  pointer = 1
  
  while pointer < len(list):
    queue = list[pointer:]
    list = list[0:pointer]
    list.append(queue[-1])
    queue.pop()
    list += queue
    pointer += 2

  return list