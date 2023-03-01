class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        cnt = 1
        max_cnt = 0
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        min_num = nums[0]
        for i in range(1, len(nums)):
            if min_num +  1 == nums[i]:
                cnt = cnt + 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
            min_num = nums[i]
        return max(max_cnt, cnt)
