class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        print(res)
        return res
    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i < len(s)):
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            start = i + 1
            end = int(length) + i + 1
            word = s[start:end]
            res.append(word)
            i = end
        return res

