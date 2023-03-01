# [212](https://leetcode.com/problems/word-search-ii/)      | Word Search II       | Tree                | <span style="color:red">Hard</span>   |
**Trie Data Structure**
  - Trie is a data structure to save and retrieve string efficiently. Used for Search keywords auto completion
  - Trie has benefit on TC, but less SC because all the pointers to child node have to be saved.
  
**Trie Time Complexity**
  - Save : O(N+L), N: number of words, L: length of word
  - Retrieve : O(L) 
  
**Trie with Class**
```
class Trie:
    def __init__(self):
        self.children = {} # why dictionary ? 
        self.word = None

def builTrie_class():
    root = Trie()
    for word in words:
        node = root
        for ch in word:
            node = node.children.setdefault(ch, Trie())
        node.word = word
 ```
 
**Trie with dictionary**
- I think using dictionary has less runtime than class. 
```
def builTrie_dict():        
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word
```
            
**What I Learned**
- dictionary
  - Check Empty : `if not dict `
  - If key doesn't exist, set default value. it returns value by default : `node.children.setdefault(ch, Trie())`

- Trie data structure which is really useful for string
- Always remember to remove duplicate operation. In this case, check this part. 
  ```
  def backtracking():
      ...
      # If there's no child, we don't need to check again
      if not node.children: 
          del prev.children[letter]
      ...
   ```


# [46](https://leetcode.com/problems/group-anagrams/)       |      Group Anagrams       |   String    | <span style="color:orange">Medium</span> |
- I tried Brute force at first, but TLE.
- Next, I tried using dictionary as a key with sorted string and append its anagrams in the list. 

**Answer code**
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            d.setdefault(key, []).append(s)
        
        return d.values()

```





