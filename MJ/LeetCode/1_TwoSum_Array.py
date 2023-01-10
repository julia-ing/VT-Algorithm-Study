# 1. TwoSum (Array)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = 0
        res = [0, 0]
        for i, num in enumerate(nums): 
            target_sub_num = target - num;
            if target_sub_num==num and nums.count(num)!=2:
                continue
            if target_sub_num in nums: 
                res[count] = i
                count += 1
            if count == 2:
                break
        return res