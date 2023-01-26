class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i=0
        max_len = 0
        for j, a in enumerate(s):
            # if i == j: continue -> 이 조건을 뺴야 통과함 
            if s[j] in s[i:j]:
                for k, b in enumerate(s[i:j+1]): 
                    if b == s[j]:
                        i=i+k+1
                        break

            if max_len <= j-i+1:
                max_len = j-i+1

        return max_len
    
    

'''
# googling
1. enumerate 순서
'''