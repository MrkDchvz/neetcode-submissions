class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for c in s:
            hm[c] = hm.get(c, 0) + 1
        for c in t:
            if c not in hm or hm.get(c) <= 0:
                return False
            if c in hm:
                hm[c] -= 1
        return True


        