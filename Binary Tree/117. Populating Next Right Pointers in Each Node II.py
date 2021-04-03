from collections import deque


# Definition for a Node.
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

        # find next node to be linked in node.children's level
        node_next = None  # will be None if nothing found in the loop below
        p = node.next
        while p is not None:
            if p.left is not None:
                node_next = p.left
                break
            if p.right is not None:
                node_next = p.right
                break
            p = p.next

        # check node.children cases
        if node.left is not None and node.right is not None:
            node.left.next = node.right
            node.right.next = node_next
        elif node.left is not None and node.right is None:
            node.left.next = node_next
        elif node.left is None and node.right is not None:
            node.right.next = node_next

        self.DFS(node.left)
        self.DFS(node.right)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        self.BFS(root)

        # self.DFS(root)

        return root
