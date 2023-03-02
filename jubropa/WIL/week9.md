## 212_Word Serch II

- 이래저래 해보다가 결국 혼자서 풀지는 못했고, 링크의 답안을 클론 코딩한다는 느낌으로 받아쓰기를 했습니다.(https://leetcode.com/problems/word-search-ii/submissions/907737256/)
- 사실 이전에 [139. Word Break](https://leetcode.com/problems/word-break/description/) 문제를 풀 때 멀쩡한 답 냅두고 다른 풀이로 풀어보겠다며 오기를 부리다 Trie 개념을 접한 바 있는데, 당시에 잘 이해하고 넘어갔더라면 이번에 스스로 풀 수 있지 않았을까 아쉬움이 남습니다.

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]
            word = cur.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                root.pop(letter)
                
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
            
        m, n = len(board), len(board[0])
        res = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return res
```

## 46_Group Anagrams_String

- 처음에는 Counter 라이브러리로 각 단어 별 글자 수를 세고 값이 같으면 같은 단어를 같은 배열에 넣는 풀이를 시도하다가 뭔가 아닌 것 같아서 넘어갔습니다.
- 다른 풀이를 보다가 문자열 자체를 정렬해버리면 Counter를 통해 글자 수를 세려 했던 것과 같은 의도(=해당 문자열을 이루는 구성요소들만을 기준으로 동일성을 확인할 수 있도록 하는 것)를 보다 쉽게 구현할 수 있음을 알게 되어 이를 차용하였습니다.

```python
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            table[key].append(word)

        result = list(table.values())

        return result     
```