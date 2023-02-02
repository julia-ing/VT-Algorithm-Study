class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
                    break
                  
        # if no item, return empty list  
        return []