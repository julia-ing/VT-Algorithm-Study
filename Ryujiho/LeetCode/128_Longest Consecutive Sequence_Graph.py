class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        nums_set = set(nums)
        maxLen = 0
        for num in nums_set:
            if num-1 not in nums_set: ## must be the minimum
                count = 1
                while (num+1) in nums_set:
                    num += 1
                    count += 1
                maxLen = max(maxLen, count)
        return maxLen
