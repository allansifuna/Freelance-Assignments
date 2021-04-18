class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tempTree = BinaryTree(newNode)
            tempTree.rightChild = self.rightChild
            self.rightChild = tempTree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def printTree(self):
        """ current -> left -> right (along with None's)"""
        print(self.key)
        if self.leftChild == None:
            print(self.leftChild)
        else:
            self.leftChild.printTree()
        if self.rightChild == None:
            print(self.rightChild)
        else:
            self.rightChild.printTree()

    def preOrder(self):
        """ current -> left -> right """
        if self.key:
            print(self.key)
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

    def postOrder(self):
        """ left -> right -> current """
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        if self.key:
            print(self.key)

    def inOrder(self):
        """ left -> current -> right """
        if self.leftChild:
            self.leftChild.inOrder()
        if self.key:
            print(self.key)
        if self.rightChild:
            self.rightChild.inOrder()
