class Solution:

    def encode(self, strs: List[str]) -> str:
        returnStr = ''
        for s in strs:
            returnStr += f"{len(s)}#{s}"


        return returnStr


    def decode(self, s: str) -> List[str]:
        i = 0
        returnArr = []
        while (i < len(s)):
            lengthStr = ''
            while s[i] != '#':
                lengthStr += s[i]
                i += 1
            if s[i] == '#':

                start = i + 1
                end = i + int(lengthStr) + 1

                returnArr.append(s[start:end])
                i = end
        return returnArr

