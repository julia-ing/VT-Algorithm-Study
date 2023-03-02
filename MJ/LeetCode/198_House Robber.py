class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0,0]
        for i, n in enumerate(nums): 
            money = dp[i] + n
            print(money)
            if money > dp[i+1]:
                dp.append(money)
            else: 
                dp.append(dp[i+1])
        
        return dp[-1]