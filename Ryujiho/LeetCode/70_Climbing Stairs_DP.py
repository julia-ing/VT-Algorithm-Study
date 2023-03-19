class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 1
        for i in range(n-1):
            temp = step1
            step1 = step1 + step2
            step2 = temp
        return step1

'''
n = 1 / ans = 1
n = 2 / ans = 2
n = 3 / ans = 1+2=3
n = 4 / ans = 3+2=5

이전 두 개의 값만 알고 있으면 된다.
'''
