class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) - 1:
            sLen = ""
            while s[i] != "#":
                sLen += s[i]
                i += 1
            
            print(i)
            
            start = i + 1
            print(start)
            
            end = i + int(sLen) + 1

            res.append(s[start:end])

            i = end
        
        return res

            
        
