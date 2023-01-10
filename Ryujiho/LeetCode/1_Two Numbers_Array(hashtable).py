class Solution(object):

  def twoSum(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    h_table = {}
    for i in range(len(nums)):
      diff = target - nums[i]
      if nums[i] in h_table:
        return [h_table[nums[i]], i]
      h_table[diff] = i
   
    # if no item, return empty list     
    return []