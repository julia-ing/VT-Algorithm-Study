class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(wordDict)
        dp=list()
        dp.append([s])
        curr_try=0

        for word in wordDict:
            string_curr.replace(word,"")
        

        while any(dp[curr_try]):
            curr_try+=1
            dp.append(list())
            for i in range(n):
                for string_curr in dp[curr_try-1]:
                    if string_curr and string_curr.find(wordDict[i])==0:
                        new_word=string_curr.replace(wordDict[i],"")
                        if new_word not in dp[curr_try]:
                            dp[curr_try].append(new_word)
                        if dp[curr_try][-1]=="":
                            return True
        return False