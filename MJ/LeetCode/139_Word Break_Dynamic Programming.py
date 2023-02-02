class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if s[i-len(word):i] == word: 
                    if dp[i-len(word)]: 
                        dp[i] = True

        return dp[-1]
    
'''
dp[i]의 의미: s[:i+1]이 스페이스로 segment되는 valid한 문자열이다. (T/F)

'''