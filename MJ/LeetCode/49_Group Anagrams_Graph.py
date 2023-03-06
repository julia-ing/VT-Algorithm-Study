class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # (1) 문자열을 정렬한다
        # (2) 같은 정렬 순서를 가진 문자열을 그룹화한다

        sorted_str = {}
        for s in strs:
            sort_s = ''.join(sorted(s))		
            if sort_s not in sorted_str:
                sorted_str[sort_s] = []
            sorted_str[sort_s].append(s)
        
        res = []
        for s in sorted_str:
            res.append(sorted_str[s])

        return res

'''
googling
python에서 문자열을 sorted 함수에 넣으면 리스트로 반환이되는데, 
이를 다시 문자열로 바꿔주려면 join이 필요하다. 

문제를 풀었는데, dict이 왜 graph인지 이해하지 못했었다. 
python의 dict은 graph가 내장되어 있다고 한다. 키-value가 vertex-edge구조가 되기 때문이었다.
https://jfun.tistory.com/96 
'''