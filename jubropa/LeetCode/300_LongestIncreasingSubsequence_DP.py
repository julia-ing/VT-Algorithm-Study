class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        results_arr = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j] and results_arr[i] < results_arr[j] + 1:
                    results_arr[i] = results_arr[j] + 1

        return max(results_arr)