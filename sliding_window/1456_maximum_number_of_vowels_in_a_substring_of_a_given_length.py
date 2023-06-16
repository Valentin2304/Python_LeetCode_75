class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        s1 = s[:k]
        currVowels, maxVowels = 0, 0
        for i in s1:
            if i in vowels:
                currVowels += 1

        if currVowels == k:
            return k

        if currVowels > maxVowels:
            maxVowels = currVowels
        i = 1

        while i < len(s) - k + 1:

            if s[i - 1] in vowels:
                currVowels -= 1

            if s[i + k - 1] in vowels:
                currVowels += 1

            if currVowels == k:
                return k

            if currVowels > maxVowels:
                maxVowels = currVowels
            i += 1
        return maxVowels