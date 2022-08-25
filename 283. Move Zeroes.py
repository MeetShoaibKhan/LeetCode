def moveZeros(nums):
	left = 0
	right = left + 1
	condition = len(nums)-1
	while right <= condition and left <= condition:
		
		if (nums[left] == 0 and nums[right] != 0):
			nums[left], nums[right] = nums[right], nums[left]
			left += 1
		if nums[left] != 0:
			left += 1
		right += 1


	print(nums)
moveZeros([0,1,0,3,12])
