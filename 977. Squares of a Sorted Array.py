#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:28:56 2022

@author: shoaib
"""
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(nums):
		result = []
		left = 0;
		right = len(nums) - 1

		while (left<=right):
			if nums[left] * nums[left] > nums[right] * nums[right]:
				result.append(nums[left] * nums[left])
				left = left + 1
			else:
				result.append(nums[right] * nums[right])
				right = right - 1

		return result[::-1] # Reveses the Array/List


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))