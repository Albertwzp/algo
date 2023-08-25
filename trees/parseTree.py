import sys
sys.path.append("..")
import operator
from trees.tree import BinaryTree
from base.stack import Stack

def buildParseTree(fpexp: str):
    fplist=fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        match i:
            case '(':
                currentTree.insertLeft('')
                pStack.push(currentTree)
                currentTree=currentTree.getLeftChild()
            case i if i not in '+-*/)':
                currentTree.setRootVal(eval(i))
                parent=pStack.pop()
                currentTree=parent
            case  i if i in '+-*/':
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                pStack.push(currentTree)
                currentTree=currentTree.getRightChild()
            case ')':
                currentTree=pStack.pop()
            case _:
                raise ValueError("Unknown Operator: " + i)
    return eTree

def evaluate(parseTree: BinaryTree):
    opers = {'+':operator.add, '-':operator.sub,
             '*':operator.mul, '/':operator.truediv}
    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()
    if leftC and rightC:
        fn=opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

if __name__ == "__main__":
    exp="( ( 7 * 9 ) + ( 2 - 5 ) )"
    bt=buildParseTree(exp)
    print(evaluate(bt))