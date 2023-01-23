class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1: return 1
        max_length = 0
        curr_string = ""
        for c in s:
            curr_string += c
            if c in curr_string[:-1]:
                curr_string=curr_string[curr_string.index(c)+1:]
            n = len(curr_string)
            max_length = n if n > max_length else max_length
        return max_length