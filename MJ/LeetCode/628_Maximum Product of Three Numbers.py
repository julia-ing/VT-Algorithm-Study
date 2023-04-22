class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      # 정렬된 순서 조합 (모든 경우의 수 조회, brute-force)
      # O(n^2)
      # ans = nums[0]
      # for i in range(len(nums)):
      #     result = nums[i]
      #     ans = max(ans, result)
      #     for j in range(i+1, len(nums)):
      #         result *= nums[j]
      #         ans = max(ans, result)

      dp = [1]
      ans = nums[0]
      for i in range(len(nums)): 
        temp_res = set()
        for prev in dp:
          temp_res.add(prev*nums[i])
        temp_res.add(nums[i])
        dp = list(temp_res)
        ans = max(max(temp_res), ans)
      
      return ans

      # 2,3,-2,4
      # 2
      # 2*3
      # 2*3*-2
      # 2*3*-2*4
      #   3
      #   3*-2
      #   3*-2*4
      #     -2
      #     -2*4
      #        4
    # 최적의 값을 찾아야 한다 -> dp?
    # dp[i]는 i로 끝나는 subarray 중에서 제일 큰 multiple-value라고 정의해보자.
    # dp[i] = max(dp[i-1]*nums[i], nums[i])
    