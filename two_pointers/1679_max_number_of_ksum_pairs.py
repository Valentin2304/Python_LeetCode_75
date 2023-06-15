class Solution:
    def maxOperations(self, nums: list[int], k) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        nums.sort()

        while left < right:
            s = nums[left] + nums[right]

            if s == k:

                count += 1
                left += 1
                right -= 1

            elif s < k:
                left +=1

            else:
                right -= 1

        return count

