class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        subarr = []
        i = 0
        result = 0

        is_zero_in = False
        while i < len(nums):
            if nums[i] == 0 and is_zero_in == False:
                subarr.append(0)
                is_zero_in = True
                i += 1

            elif nums[i] == 1:
                subarr.append(1)
                i += 1

            elif nums[i] == 0 and is_zero_in == True:
                count = 0
                for j in range(0, len(subarr)):
                    if subarr[j] != 0:
                        count += 1
                    else:
                        count += 1
                        break
                for k in range(count):
                    subarr.pop(0)

                subarr.append(0)
                i += 1

            if is_zero_in and result < len(subarr)-1:
                result = len(subarr)-1

            elif is_zero_in == False and result < len(subarr):
                result = len(subarr) - 1


        return result

