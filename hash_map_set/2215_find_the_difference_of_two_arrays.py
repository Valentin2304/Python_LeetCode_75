class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        r1 = [n for n in nums1 if n not in nums2]
        r2 = [n for n in nums2 if n not in nums1]

        return [set(r1), set(r2)]
