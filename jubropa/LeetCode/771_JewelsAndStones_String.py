from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        res = 0

        counter = Counter(stones)
        for jewel_type in jewels:
            res+=counter[jewel_type]

        return res