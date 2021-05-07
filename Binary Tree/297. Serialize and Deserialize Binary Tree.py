# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.code = ""

    def DFS(self, node):
        if node is None:
            self.code += "N,"
            return

        self.code += "{},".format(node.val)
        self.DFS(node.left)
        self.DFS(node.right)

    def deDFS(self, arr):
        """
        Note pop(0) at alpha.
        Let data = [1, N, 2, N, N].
        To build the left subtree, the parameter is [N, 2, N, N].
        To build the right tree, the parameter should be [2, N, N].
        However, if we do not pop arr[0] out here, the parameter will still be [N, 2, N, N].
        """
        if arr[0] == "N":  # no need to consider empty arr, the end of arr is always an "N"
            return None

        # generate node
        node = TreeNode(int(arr[0]))
        arr.pop(0)
        # generate left
        node.left = self.deDFS(arr)
        arr.pop(0)  # alpha
        # generate right
        node.right = self.deDFS(arr)

        return node

    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.DFS(root)
        return self.code[:-1]  # remove the last comma, code = "1,2,N,"

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        return self.deDFS(arr)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
