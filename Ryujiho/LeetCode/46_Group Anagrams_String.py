class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            d.setdefault(key, []).append(s)
        
        
        return d.values()
