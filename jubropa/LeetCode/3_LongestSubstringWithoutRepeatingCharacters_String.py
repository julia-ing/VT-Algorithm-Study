class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = cnt = 0
        filter = set()

        for idx in range(len(s)):
            for char in s[idx:]:
                if char not in filter:
                    cnt+=1
                    filter.add(char)
                    result = cnt if result < cnt else result
                else:
                    filter.clear()
                    cnt = 0
                    break

        return result
            
        
