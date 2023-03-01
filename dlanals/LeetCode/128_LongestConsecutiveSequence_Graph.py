class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        cnt = 1
        max_length = 1

        if len(nums) == 0: return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if cnt > max_length : max_length = cnt
                cnt = 1
            
        return max(cnt, max_length)
