class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])

        def buildTrie():
            for word in words:
                node = root
                for ch in word:
                    node = node.children.setdefault(ch, Trie())
                node.word = word
        
        # check all string words at once 
        def backtracking(node, index, visited):
            i,j = index
            letter = board[i][j]
            if index in visited: return
            if letter not in node.children: return

            prev = node
            node = node.children[letter]

            if node.word:
                answer.add(node.word)
            
            # If there's no child, we don't need to check again
            if not node.children: 
                del prev.children[letter]
            
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                di, dj = i+dir[0], j+dir[1]
                if di<0 or dj<0 or di>=n or dj>=m: continue

                # union() = inplace=False & return values
                backtracking(node, (di,dj), visited.union({(i, j)}))

        ## Main 
        root = Trie()
        buildTrie()
        answer = set()
        
        # check all possible starting point
        for i in range(n):
            for j in range(m):
                backtracking(root, (i, j), set() )

        return answer      
