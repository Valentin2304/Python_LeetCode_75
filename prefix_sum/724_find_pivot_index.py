class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == sum(nums[i+1:]):
                return i
            left_sum += nums[i]
        return -1