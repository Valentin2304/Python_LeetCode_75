class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        def div(dd):
            if n % len(dd) == 0: return str1 == dd * (n // len(dd))

        res = ""
        cur = ""
        for i in range(m):
            cur += str2[i]
            if cur * (m // (i + 1)) == str2 and div(cur):
                res = cur

        return res



