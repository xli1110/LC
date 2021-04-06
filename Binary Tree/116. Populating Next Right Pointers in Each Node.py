from collections import deque


# # Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def BFS(self, root):
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()

                node.next = q[0] if i != length - 1 else None

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

    def DFS(self, node):
        if node is None:
            return

        if node.left is not None:  # node has two children
            node.left.next = node.right  # link left child
            node.right.next = node.next.left if node.next is not None else None  # link right child

        self.DFS(node.left)
        self.DFS(node.right)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            # raise Exception("Empty Tree")
            return None

        # self.BFS(root)

        self.DFS(root)
        return root
