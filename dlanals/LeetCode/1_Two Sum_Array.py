class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target: return [i, j]
        # But O(n^2)
        
        # Using dictionary {element : index}
        d = {}
        for i, j in enumerate(nums):
            m = target - j
            if m in d:
                return [d[m], i]
            else: d[j] = i
