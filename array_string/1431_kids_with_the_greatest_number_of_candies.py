class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candy = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result
