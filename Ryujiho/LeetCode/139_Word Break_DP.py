class Solution(object):
    def wordBreak(self, s, wordDict):
        N = len(s) + 1
        chk = [False] * N
        chk[0] = True

        for i in range(1, N):
            for w in wordDict:
                if s[i-len(w):i] == w and chk[i-len(w)]:
                    chk[i] = True
                  
        return chk[N-1]

#check1. mark when matched word ends -> it means new start point
#check2. see if any word in lists matches
# TC(NM), N:str.length, M: wordDict.length