class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        i = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n == 0: return True
            if flowerbed[0] == 0 and n <= 1: return True
            return False

        while i < len(flowerbed):
            if i == 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
                    i += 1
                    continue

            if i == len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
                    i += 1
                    continue

            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
                i += 1
                continue

            i += 1


        if count < n:
            return False
        return True


