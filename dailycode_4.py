

#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space. In othe
#words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
#negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place.


list = [3, 4, -1, 1]


def findMissingPosInt(list):
    list = [x for x in list if x >= 0]
    list = sorted(list)
    for i in range(len(list)):
        if i == (len(list) - 1):
            print (list[-1] + 1)
            break;
        if list[i + 1] > list[i] + 1:
            print(list[i] + 1)
            break;

findMissingPosInt(list)
