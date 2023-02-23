## 3_Longest Substring Without Repeating Characters_String

- 2중 반복문을 사용했으며, 입력값 문자열에 대한 반복문과, 입력값 문자열 내의 각 인덱스에서부터 Substring의 길이를 세어나가기 위한 반복문으로 구성됐습니다.
- 하위 반복문에서 Substring의 길이를 세어나가다가 중복된 문자를 발견하면(=filter에 char이 있으면) 하위 반복문을 깨고 상위 반복문으로 돌아간 후, 다음 인덱스에서 다시 하위 반복문으로 돌아와 Substring의 길이를 세어나갑니다.
- 풀면서도 세련된 풀이는 아니라고 생각했는데, 다른 풀이들을 보니 생각 이상으로 많이 투박한 풀이였습니다.
- 모범 답안으로 추정되는 슬라이딩 윈도우를 활용한 풀이가 굉장히 세련되보여서 마음에 들었습니다. (https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3024764/python-sliding-window-approach-99-17-faster-sc-o-1/)

```python
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = cnt = 0
        filter = set()

        for idx in range(len(s)):
            for char in s[idx:]:
                if char not in filter:
                    cnt+=1
                    filter.add(char)
                    result = cnt if result < cnt else result
                else:
                    filter.clear()
                    cnt = 0
                    break

        return result
```

- Golang에 익숙해질 겸 로직을 그대로 Golang으로 옮겨적었습니다.

``` Golang
func lengthOfLongestSubstring(s string) int {

	result, cnt := 0, 0
	filter := map[rune]int{}

	for idx := range s {
		for _, char := range s[idx:] {
			_, exist := filter[char]
			if !exist {
				cnt += 1
				filter[char] = 1
				if result < cnt {
					result = cnt
				}
			} else {
				filter = map[rune]int{}
				cnt = 0
				break
			}
		}
	}

	return result
}
```

## 139_Word Break_DP

- 이미 DP 등을 이용한 다른 풀이를 봤음에도 처음 떠올렸던 접근 방식에 대한 미련을 버리지 못해 계속 도전하다가, 시간을 너무 많이 써서 포기하려던 차에 처음 떠올렸던 접근 방식이 Trie라는 자료구조를 활용한 풀이와 흡사하다는 걸 알았습니다. 다만, 해당 풀이를 아직 세세히 이해하진 못해서 일단은 코드를 그대로 사용했습니다. (https://leetcode.com/problems/word-break/solutions/1455100/python-3-solutions-top-down-dp-bottom-up-dp-then-optimised-with-trie-clean-concise/)
- 알고리즘에 대한 기반이 빈약하다보니 알고리즘 문제를 풀 때 마다 정석적이고 깔끔한 것과는 거리가 먼 풀이를 떠올리곤 하는데, 이번에도 그 탓에 필요 이상으로 시간을 너무 많이 잡아먹은 것 같아 기반을 다질 필요성을 느끼고 있습니다.
- 이것도 Golang으로 옮겨 적어보려 했는데, Golang과 해당 풀이에 대한 이해가 부족한 탓인지 정답이 자꾸 틀리게 나와 일단은 보류 중입니다.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = self.TrieNode()
        for word in wordDict:
            root.addWord(word)
            
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            cur = root
            for j in range(i+1, n+1):
                c = s[j-1]
                if c not in cur.child: 
                    break  # s[i:j] not exist in our trie
                cur = cur.child[c]
                if cur.isWord and dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]

    class TrieNode:
        def __init__(self):
            self.isWord = False
            self.child = defaultdict(Solution().TrieNode)
        
        def addWord(self, word):
            cur = self
            for c in word:
                cur = cur.child[c]
            cur.isWord = True
```