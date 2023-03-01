class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        res = 0

        for i in nums_set:

            if i - 1 not in nums_set:
                num = i 
                length = 1

                while num + 1 in nums_set:
                    num += 1
                    length += 1
                
                res = max(length, res)

        return res
        
