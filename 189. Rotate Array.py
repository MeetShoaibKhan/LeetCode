#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:28:56 2022

@author: shoaib
"""
# Link: https://leetcode.com/problems/rotate-array/

def rotate(nums, k):
	k = k % len(nums)
	left = 0
	right =  len(nums) - 1

	while left <= right:
		nums[left], nums[right] = nums[right], nums[left]
		left, right = left + 1, right - 1 


	left = 0
	right = k - 1
	while left <= right:
		nums[left], nums[right] = nums[right], nums[left]
		left, right = left + 1, right - 1 


	left = k
	right = len(nums) - 1
	while left <= right:
		nums[left], nums[right] = nums[right], nums[left]
		left, right = left + 1, right - 1 
	


	print(nums)





rotate([1,2],3)