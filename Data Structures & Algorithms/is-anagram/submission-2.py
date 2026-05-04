from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = Counter(s)
        
        for c in t:
            if c in my_dict:
                if my_dict[c] == 0:
                    return False
                else:
                    my_dict[c] -= 1
            else:
                return False
        return True 
            



        
        