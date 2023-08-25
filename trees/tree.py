from typing import List

class BinaryTree(object):
    def __init__(self,x: object):
        self.key=x
        self.left=None
        self.right=None

    def insertLeft(self,x: object):
        if self.left==None:
            self.left=BinaryTree(x)
        else:
            t=BinaryTree(x)
            t.left=self.left
            self.left=t

    def insertRight(self,x: object):
        if self.right==None:
            self.right=BinaryTree(x)
        else:
            t=BinaryTree(x)
            t.right=self.right
            self.right=t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, x: object):
        self.key=x

    def getRootVal(self):
        return self.key