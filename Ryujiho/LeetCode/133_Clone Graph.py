from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        # BFS to traverse
        q = deque([node]) 

        # HashMap to check visited
        clones = { node.val: Node(node.val, []) } 

        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for nbr in cur.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    q.append(nbr)
                cur_clone.neighbors.append(clones[nbr.val])

        return clones[node.val]
