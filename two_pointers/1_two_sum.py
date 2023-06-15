class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        left = 0
        right = len(nums) - 1

        nums_sorted = nums.copy()
        nums_sorted.sort()

        result = []

        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]

            if current_sum == target:

                for j in range(0, len(nums)):
                    if nums[j] == nums_sorted[left]:
                        result.append(j)
                        break
                for i in range(len(nums)-1, -1, -1):
                    if nums[i] == nums_sorted[right]:
                        result.append(i)
                        break
                return result

            elif current_sum < target:
                left += 1

            else:
                right -= 1


s = Solution()
print(s.twoSum([2,7,11,15], 9))