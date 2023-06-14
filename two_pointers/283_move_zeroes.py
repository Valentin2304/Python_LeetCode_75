class Solution(object):
    def moveZeroes(self, nums):
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums


#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.