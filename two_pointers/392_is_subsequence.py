class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True
        if len(s) == 1 and s[0] not in t: return False
        if len(s) == 1 and s[0] in t: return True

        seq = 0
        indexes = []

        for i in range(0, len(t)):

            if t[i] == s[seq]:

                seq += 1
                indexes.append(i)

                if len(indexes) == len(s):
                    return True

        if len(indexes) < len(s):
            return False

        return True




#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

