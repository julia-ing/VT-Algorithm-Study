class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == 1: return nums

        count = {}
        for i in nums:
            if i in count: count[i] +=1
            else: count[i] = 1
        sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)

        answer = [ num for num, cnt in sorted_count[:k] ]
        return answer


# Runtime 70 ms
