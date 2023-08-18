from typing import List

class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    def __repr__(self):
        return

def createBTree(data: List[int],index: int):
    pNode=None
    if index<len(data):
        if data[index]==None:
            return
        pNode=TreeNode(data[index])
        pNode.left=createBTree(data, 2*index+1)
        pNode.right=createBTree(data, 2*index+2)
    return pNode

class Solution:
    def maxDepth_dfs(self, root: TreeNode)->int:
        if not root: return 0
        return max(self.maxDepth_dfs(root.left),self.maxDepth_dfs(root.right))+1
    def maxDepth_bfs(self, root: TreeNode):
        if not root: return 0
        queue,res = [root],0
        while queue:
            tmp=[]
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue=tmp
            res+=1
        return res
    
    def isBalance(self, root: TreeNode):
        def recur(root):
            if not root: return 0
            left=recur(root.left)
            if left==-1: return -1
            right=recur(root.right)
            if right==-1: return -1
            return max(left,right)+1
        return recur(root) != -1


if __name__ == '__main__':
    lst=[5,4,8,11,None,13,4,7,2,None,None,None,1,2,7,3,6,78,9,8]
    root=createBTree(lst,0)
    so=Solution()
    maxDepth=so.maxDepth_bfs(root)
    isB=so.isBalance(root)
    print(maxDepth,isB)