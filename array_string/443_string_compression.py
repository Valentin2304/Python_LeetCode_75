class Solution:
    def compress(self, chars: list[str]) -> str:
        dictionary = {}
        result = []
        for i in range(len(chars)):
            if chars[i] in dictionary.keys():
                dictionary[chars[i]] += 1
            else:
                dictionary[chars[i]] = 1
        for k, v in dictionary.items():
            if v > 1:
                result.append(k)
                result.append(v)
            else:
                result.append(k)

        chars = "".join([str(c) for c in result])
        return len(chars)


#Incorrect description
