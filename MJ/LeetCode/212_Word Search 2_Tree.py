class Trie:
    def __init__(self, end=None):
        self.end = end
        self.child = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]

        len_x = len(board)
        len_y = len(board[0])
        visited = set()
        res = set()

        def dfs(i, j, node):
            if node.end is not None:
                res.add(node.end)

            if not node.child: # time limit key 
                return

            for k in range(4):
                x2, y2 = i + dx[k], j + dy[k]
                if 0<=x2<len_x and 0<=y2<len_y:
                    if board[x2][y2] in node.child and (x2, y2) not in visited: 
                        visited.add((i,j))
                        dfs(x2, y2, node.child[board[x2][y2]])
                        visited.remove((i,j))

            return
        
        head = Trie("") # init

        for word in words: # Trie with words
            node = head
            for i in range(len(word)):
                a = word[i]
                if a not in node.child:
                    node.child[a] = Trie()
                node = node.child[a]
            node.end = word        

        for i in range(len_x):
            for j in range(len_y):
                visited = set()
                if board[i][j] in head.child:
                    dfs(i,j, head.child[board[i][j]])

        return res

    