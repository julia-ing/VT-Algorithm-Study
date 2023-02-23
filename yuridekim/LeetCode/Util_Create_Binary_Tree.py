# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(inp):
    prev = []
    nextPrev = []
    temp= []
    nextIn = 0
    
    rootNode = TreeNode(inp[nextIn])
    nextIn += 1
    prevNode = rootNode
    prev.append(rootNode)
    prevIndex = 0
    while prevIndex < len(prev):
        nextNode = prev[prevIndex]
        prevIndex += 1
        if nextNode is not None:
            if nextIn < len(inp):
                left = inp[nextIn]
                nextIn += 1
                leftNode = None
                if left is not None:
                    leftNode = TreeNode(left)
                nextNode.left = leftNode
                if leftNode is not None:
                    nextPrev.append(leftNode)
                
            # if there is a right child, then process
            if nextIn < len(inp):
                right = inp[nextIn]
                nextIn += 1
                rightNode = None
                if right is not None:
                    rightNode = TreeNode(right)
                nextNode.right = rightNode
                if rightNode is not None:
                    nextPrev.append(rightNode)
                               
        if prevIndex >= len(prev):
            temp = prev
            prev = nextPrev
            nextPrev = temp
            nextPrev.clear()
            prevIndex = 0
    
    return rootNode

"""
For future reference
tree_str = "5,3,6,2,4,null,null,1" # input list of node values without brackets
node_list = list(tree_str.split(",")) # split nodes
node_list = [int(a) if a.isdigit() else None for a in node_list] # map string to digits
tree = create_tree(node_list) # create tree with util
"""