class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount+1
        dp = [MAX for i in range(MAX)] # current number of coins
        dp[0] = 0 # set a default value

        for i in range(1,MAX): # fill in the order from 1 to amount
            for coin in coins: # check the minimum count with all coins
                if i==coin: # if same, set 1 count
                    dp[i]=1
                    break
                
                # if diff value exists
                diff = i-coin
                if diff>=0:
                    # Keep or Add 1 count from the previous amount's count
                    dp[i]= min(dp[i],1+dp[diff])

        return -1 if dp[-1]==MAX else dp[-1]   

'''
TC(Time Complexity): O(amount * len(coins))
SC(Space Complexity): O(amount)
'''                             
