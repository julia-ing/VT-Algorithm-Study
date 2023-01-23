from collections import deque
class Solution:
    def wordBreak(self, s, wordDict):
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

sol=Solution()
print(sol.wordBreak("leetcode",["leet","code"]))