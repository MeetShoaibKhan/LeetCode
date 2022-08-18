#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:08:19 2022

@author: shoaib
"""
# Link: https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# The commented code below summited to leetcode which have the api  

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         left = 0
#         right = n
#         middle = int((left+right)/2)
        
#         while left <= right:
#             if not isBadVersion(middle):
#                 left = middle + 1
#             else:
#                 right = middle - 1
#             middle = int((left+right)/2)
            
#         return right + 1 



#since i didnt have the isBadVersion() api locally i created an isBadVersion list,
# which have boolean values to act as an api.
def firstBadVersion(n):

	left = 0
	right = n
	middle = int((left+right)/2)
 
	isBadVersion = [ False, False, False, True, True,  True, True,  True, True,  True, True,  True, True,  True, True]
        
        
	while left <= right:
		if not isBadVersion[middle]:
			left = middle + 1
			
		else:
			right = middle - 1

		middle = int((left+right)/2)
	return right + 1 



print(firstBadVersion(15))