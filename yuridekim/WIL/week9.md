### **Week 9**
|                                  #                                   |            TITLE             |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:----------------------------------------:|
| [212](https://leetcode.com/problems/word-search-ii/)      | Word Search II       | Tree                | <span style="color:red">Hard</span>   |
|       [46](https://leetcode.com/problems/group-anagrams/)       |      Group Anagrams       |   String    | <span style="color:orange">Medium</span> |

### 212. Word Search
#### 문제풀이
```
class Solution(object):
    def findTree(self, board, word, visited, m, n):
        if word == "":
            return True
        i = visited[-1][0]; j = visited[-1][1]
        candidates = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        for cand in candidates:
            if cand not in visited and 0<=cand[0] and cand[0]<m and 0<=cand[1] and cand[1]<n and board[cand[0]][cand[1]] == word[0]:
                temp_visited = list(visited); temp_visited.append(cand)
                temp_result = self.findTree(board, word[1:], temp_visited, m, n)
                if temp_result:
                    return True
        return False
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result_list = []
        m = len(board); n = len(board[0])
        flat_list = [item for sublist in board for item in sublist]
        for word in words:
            print(word)
            idx = 0
            while word[0] in flat_list[idx:]:
                visited = []
                idx += flat_list[idx:].index(word[0])
                visited.append((idx//n, idx % n))
                found = self.findTree(board, word[1:], visited, m, n)
                if found:
                    result_list.append(word)
                    break
                idx += 1
                        
        return result_list
```
처음에는 단순구현을 해줬다. words로 들어오는 단어마다 board에 있는 character들을 가지고 완성해줄 수 있는지 확인을 해줬다. 일단 첫 글자가 board에 있는지 확인 후 그 다음부터 각 위, 아래, 왼쪽 오른쪽을 탐색해주며 해당 board가 word의 다음 character인지 확인을 해줬다. 논리상으로는 맞는 것 같은데 다음과 같은 테스트 케이스에서 타임 에러가 났다.
ababababaa
ababababab
ababababac
ababababad
ababababae
ababababaf
ababababag
ababababah
ababababai
ababababaj
위 테스트케이스에서는 676개의 word들을 모두 일일히 확인해야했기 때문에 시간이 너무 오래걸렸다.
이렇게 앞은 같은(겹치는) word들이 있을 걸 대비해 따로 자료구조로 저장을 해놔야할 것 같았다.

#### 💡 What I learned!
그래서 solution들에 있는 hint를 참고해서 Trie를 이용했다.
```
import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return 
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
```
들어오는 모든 word들에 대해서 순서대로 child로 갖고 있도록 trie node를 만들어주고 이때 단어별로 isWord로 우리가 찾고 있는 단어인지를 탐색해준다.
따라서 시간을 향상시키며 많은 메모리를 소비하게 될 것이다.
시간 복잡도는 다음과 같다.
O((단어 갯수 * 단어 최대 길이) * (보드 세로 * 보드 가로))
내 기본 알고리즘과 비교했을 때 나는 보드에 있는 모든 값들을 기본으로 탐색해주지 않기 때문에 word 개수가 작을 때 유리할 것 같고 반대로 trie는 반복되는 문자열이 있는 단어가 아주 많을 때 시간을 효과적으로 줄일 수 있을 것 같다.


-------------------------------------------------------------------
### 46. Group Anagrams
#### 문제풀이

```
class Solution(object):
    def enumerateChar(self, word):
        char_arr = [0] * 26
        for char in word:
            char_arr[ord(char)- 97] += 1
        return char_arr
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        enum_arr = [self.enumerateChar(strs[0])]
        result_list = [[strs[0]]]
        del strs[0]
        for str in strs:
            str_arr = self.enumerateChar(str)
            if str_arr in enum_arr:
                result_list[enum_arr.index(str_arr)].append(str)
            else:
                enum_arr.append(str_arr)
                result_list.append([str])
        return result_list
```
anagram을 확인해주기 위해 각 단어들의 알파벳 occurence 횟수를 확인해줬다. 그리고 26개 알파벳의 횟수 list가 이미 있으면 거기에 해당하는 단어들과 모두 묶어주고 새로운 occurence라면 새로운 list를 형성시켜줬다.


#### 💡 What I learned!
Runtime 1409 ms
Beats 8.42%

Memory 19.7 MB
Beats 24.21%

내 원래 알고리즘에서 둘 다 성능이 너무 안 좋아서 solution을 같이 확인해줬다.

```
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())
```
단순히 word를 sort시켜줘서 grouping을 해주면 되는거였다.

Runtime 96 ms
Beats 87.76%

Memory 18 MB
Beats 52.34%
쉬운 문제를 너무 어렵게 생각한 것 같다.