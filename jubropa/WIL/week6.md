## 5_Longest Palindromic Substring

- 보류...

## 347_Top_K_Frequent_Elements

- 알고리즘 풀이의 핵심이 논리력이니만큼 이런 풀이가 권장되지는 않으리라 생각되지만, 시간이 부족한 관계로 떠오르는 가장 단순한 방법을 구현하였습니다.

``` python
    import collections

    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            counter = collections.Counter(nums)
            sorted_counter = sorted(counter.items(), key=lambda key_val_pair:key_val_pair[1], reverse=True)

            return [key_val_pair[0] for key_val_pair in sorted_counter[:k]]
```