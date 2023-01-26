class Solution(object):

  def lengthOfLongestSubstring(self, s):
    maxLen = 0
    q = []
    for i in s:
      if i not in q:
        q.append(i)
      else:
        idx = q.index(i)
        del q[:idx + 1]
        q.append(i)

      maxLen = max(maxLen, len(q))

    return maxLen
