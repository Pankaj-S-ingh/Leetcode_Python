from symbol import return_stmt
from turtle import right


class Solution:
    def isSymmetric(self,root:TreeNode)->bool:
        if root is None:
            return True
        return self.ismirror(root.left,root.right)
    def ismirror(self,leftroot,rightroot):
        if leftroot and rightroot:
            return leftroot.val==rightroot.val and self.ismirror(leftroot.left,rightroot.right) and self.ismirror(leftroot.right,rightroot.left)
        return leftroot==rightroot