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
        """
        When visiting a node, this DFS processes its children.

        Note recursion order, R -> L.
        self.DFS(node.right)
        self.DFS(node.left)
        """
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

        # 先确保 root.right 下的节点的已完全连接，因 root.left 下的节点的连接
        # 需要 root.left.next 下的节点的信息，若 root.right 下的节点未完全连
        # 接（即先对 root.left 递归），则 root.left.next 下的信息链不完整，将
        # 返回错误的信息。可能出现的错误情况如下图所示。此时，底层最左边节点将无
        # 法获得正确的 next 信息：
        #                  o root
        #                 / \
        #     root.left  o —— o  root.right
        #               /    / \
        #              o —— o   o
        #             /        / \
        #            o        o   o

        self.DFS(node.right)
        self.DFS(node.left)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        self.BFS(root)

        # self.DFS(root)

        return root
