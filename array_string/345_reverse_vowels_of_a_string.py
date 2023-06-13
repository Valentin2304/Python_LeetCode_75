class Solution:
    def reverseVowels(self, str1: str) -> str:
        indexes = []
        vowels = "AEUIOaeiou"
        result = ""
        count = 0
        for i in range(len(str1)):
            if str1[i] in vowels:
                indexes.append(i)

        indexes.sort(reverse=True)

        for j in range(len(str1)):

            if str1[j] in vowels:
                result += str1[indexes[count]]
                count += 1
                continue
            result += str1[j]

        return result


