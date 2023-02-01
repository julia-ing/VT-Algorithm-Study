class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = 0
        substr = ''
        for c in s:
            if c not in substr:
                substr += c
                record = max(record, len(substr))
            else:
                substr = substr.split(c)[-1] + c
        return record