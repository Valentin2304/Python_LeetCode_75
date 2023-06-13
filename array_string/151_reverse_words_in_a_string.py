class Solution:
    def reverseWords(self, s: str) -> str:

        result = s.split(" ")
        result.reverse()
        while "" in result:
            result.remove("")

        return " ".join(result)

