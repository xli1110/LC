# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def make_tree(self, val, left, right):
        n = TreeNode()
        n.val = val
        n.left = left
        n.right = right
        return n

    def DFS(self, node, tar):
        """
        Note the SLICE of self.path.
        Otherwise, self.res is appended by a reference.
        When the DFS return to previous invokes, self.path will be changed, and the values in self.res will also be changed.
        """
        if node is None:
            return

        self.path.append(node.val)
        if node.left is None and node.right is None and tar == node.val:
            self.res.append(self.path[:])

        self.DFS(node.left, tar - node.val)
        self.DFS(node.right, tar - node.val)

        self.path.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> [[int]]:
        # if root is None:
        #     raise Exception("Empty Tree")
        self.DFS(root, targetSum)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    root = sol.make_tree(1,
                         sol.make_tree(2,
                                       None,
                                       None),
                         sol.make_tree(2,
                                       None,
                                       None)
                         )
    tar = 3

    sol.pathSum(root, tar)
    print(sol.res)
