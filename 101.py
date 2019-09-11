## Grant Gasser
## LeetCode 101 Symmetric Tree
## 9/11/2019

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return False

    q = [root] # just pop(0) and its a queue
    bfs_res = []

    # BFS
    while q:
        node = q.pop(0)

        bfs_res.append(node.val)

        # left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


    i = 0
    while (2**i - 1) <= len(bfs_res):
        # sub is just each level in the tree
        sub = bfs_res[2**i - 1:(2**i - 1)+2**i]


        # check symmetry
        if sub != sub[::-1]:
            return False

        i += 1

    return True

def main():
    # test binary tree [1,2,2,3,4,4,3]
    # and [1,2,2,None,3,None,3]

    root = TreeNode(1)

    # left side
    root.left = TreeNode(2)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(3)

    # right side
    root.right = TreeNode(2)
    root.right.left = TreeNode(None)
    root.right.right = TreeNode(3)

    print(isSymmetric(root))

main()
