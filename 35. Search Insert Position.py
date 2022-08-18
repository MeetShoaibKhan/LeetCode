
"""
Created on Thu Aug 18 7:54:00 pm 2022

@author: shoaib
"""
# Link: https://leetcode.com/problems/search-insert-position


def searchInsert(nums, target) :
    left = 0
    right = len(nums)-1
    middle = int((left+right)/2)

    while left<=right:
        if nums[middle] == target:
            return middle
        elif nums[middle] > target :
            right = middle-1
        else:
            left = middle + 1
        middle = int((left+right)/2)

    if nums[middle] > target :
        return 0
    return middle + 1






# just some code to check all the possible commbination
# a = [0,1,2,3,4,5,6,7,8]
# temp = []
# for n in range(0,10):
# 	temp = list(range(0,10));
# 	temp.remove(n)

# 	print(temp,n)
# 	print(searchInsert(temp,n))
# 	print("\n")
	

print(searchInsert([1,3,5,6.7,8],2))

