# 94. Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.doGood(root, res)
        return res

    def doGood(self, root, res):
        if root:
            self.doGood(root.left, res)
            res.append(root.val)
            self.doGood(root.right, res)
        return res