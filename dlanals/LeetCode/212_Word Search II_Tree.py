class Node:
    def __init__(self):
        self.child = {}
        self.end = None  # word
        
class Tries:
    def __init__(self):
        self.root = Node()
    
    def inser_word(self, word):
        
        cur = self.root
        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                cur.child[c] = Node()
                cur = cur.child[c]
        cur.end = word

    # O(M(4(3**L-1)))
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
        # tries build tries
        # backtracking in each node
        # if neibor in node.child
        Rows, Cols = len(board), len(board[0])
        
        tries = Tries()
        visited = set()
        RR = set(range(Rows))
        CC = set(range(Cols))
        
        for word in words:
            tries.inser_word(word)
            
        words = set(words)
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        res = set()
        
        def backtracking(r, c, node):
            
            if node.end:
                res.add(node.end)
                
            if not node.child:
                return
            
            for dr, dc in direction:
                row, col = r + dr, c + dc
                if row in RR and col in CC and (row, col) not in visited and board[row][col] in node.child:
                    visited.add((row, col))
                    backtracking(row, col, node.child[board[row][col]])
                    visited.remove((row, col))
            

        for i in range(Rows):
            for j in range(Cols):
                if board[i][j] in tries.root.child:
                    visited.add((i, j))
                    backtracking(i, j, tries.root.child[board[i][j]])
                    visited.remove((i, j))
        return res
