import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda key_val_pair:key_val_pair[1], reverse=True)

        return [key_val_pair[0] for key_val_pair in sorted_counter[:k]]