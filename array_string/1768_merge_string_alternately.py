
def mergeAlternately(self, word1: str, word2: str) -> str:
    result = ""
    n = min(len(word1), len(word2))
    for i in range(n):
        result += word1[i]
        result += word2[i]
    if len(word1) < len(word2):
        result += word2[n:]
    elif len(word1) > len(word2):
        result += word1[n:]
    return result




