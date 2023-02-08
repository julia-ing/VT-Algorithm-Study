📝WEEK6

✔number1

    [처음생각한 방법 -> Test case 모두 통과, Time out]
    1. sorting을 한 후, set들을 구해서 각각 몇개를 가지고 있는 지 확인함
    2. k번째만큼 list에 append해서 return시켜줌
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        set_nums = list(set(nums))
        dict_nums = {}
        pivot = str(nums[0])

        cnt = 0

        for i in nums:
            if str(i) == pivot:
                cnt = cnt + 1
            else:
                dict_nums[pivot] = cnt
                cnt = 1
                pivot = str(i)

            dict_nums[pivot] = cnt
            sorted_dict = sorted(dict_nums.items(), key = lambda item: item[1], reverse = True)

        result = []
        for i in range(k):
            result.append(int(sorted_dict[i][0]))
        return result
       
     [정답]
     <counter를 사용할 때>
     ex_list = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi']
     ex_counter = collections.Counter(ex_list)
     print(ex_counter)

     >>> Counter({'kim': 5, 'choi': 3, 'park': 2})
  
     class Solution:
      def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
        
