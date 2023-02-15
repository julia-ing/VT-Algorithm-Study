class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return map(operator.itemgetter(0), collections.Counter(nums).most_common(k))
        # return [x[0] for x in collections.Counter(nums).most_common(k)]
        # return map(lambda x: x[0], collections.Counter(nums).most_common(k))
        # return list(zip(*collections.Counter(nums).most_common(k)))[0]