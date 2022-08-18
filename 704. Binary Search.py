#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:09:41 2022

@author: shoaib
"""
# Link: https://leetcode.com/problems/binary-search/

def search(nums, target):
    left = 0
    right = len(nums)-1
    middle = int((left+right)/2)
    
    
    while left<=right:
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
            
        middle = int((left+right)/2)
        
    return -1 
nums =  [-100,-22,-1,1,2,3,4,5,6,7,8,9,10,88,99]
target = 10

print(search(nums,target))