class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        arr_result = []
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in hm:
                hm[s_sorted] = [s]
            else:
                hm[s_sorted].append(s)
        
        for arr in hm:
            arr_result.append(hm[arr])

        return arr_result

        