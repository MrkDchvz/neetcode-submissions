class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            sLen = len(s)

            print(f"{sLen}#{s}")
            string += f"{sLen}#{s}"
            
        return string
    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        strlen = ''
        while(i < len(s)):
            if s[i].isdigit():
                strlen += s[i]
                i += 1
                continue
            if s[i] == '#':
                start = i + 1
                end = int(strlen) + i + 1            
                arr.append(s[start:end])
                i = end
                strlen = ''
        return arr
            


    


