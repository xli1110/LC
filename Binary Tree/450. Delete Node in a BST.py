# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/yong-qian-qu-huo-zhe-hou-ji-jie-dian-zi-shu-dai-ti/

        TBH, the problem does not describe the deletion rule.
        Can we delete it in any form?
        For example,
        arr = [inorder]
        arr' = arr.delete_node(node)
        then, we link arr' as a linked list which is a special form of BST.
        """
