import numpy as np
class BinaryTree:
    def __init__(self):
        self.data = [None]
        
    def insert(self, val):
        # keep track of idx we're at traversing the tree
        idx = 0
        while self.data[idx] is not None:
            idx = idx * 2 + (1 if self.data[idx] > val else 2)
            if idx >= len(self.data):
                self.data = self.data + [None]*(idx + 1 - len(self.data))
        self.data[idx] = val
        
    def find(self, val):
        idx = 0
        while self.data[idx] is not None and self.data[idx] != val:
            idx = idx * 2 + (1 if self.data[idx] > val else 2)
            if len(self.data) <= idx:
                return -1
        return idx if self.data[idx] is not None else -1
    
    def levelUp(self, idx):
        self.data[idx] = None
        leftChild = idx * 2 + 1
        rightChild = (idx + 1) * 2
        if len(self.data) > leftChild:
            if self.data[leftChild] is not None:
                self.data[idx] = self.data[leftChild]
                self.levelUp(leftChild)
            elif len(self.data) > rightChild and self.data[rightChild] is not None:
                self.data[idx] = self.data[rightChild]
                self.levelUp(rightChild)
                
    def getValues(self, level):
        values = []
        for x in range(2**level - 1, 2**(level + 1) - 1):
            if len(self.data) <= x:
                values.append(None)
            else:
                values.append(self.data[x])
        return values

from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class DFSTraversalInterator_post:
    def __init__(self,tree):
        import numpy as np
        self.tree=tree
        self.index=0
        self.visited=np.zeros(len(tree.data))
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<0:
            raise StopIteration()
        print(self.index)
        flag1=True
        flag2=True
        while flag1 or flag2:
            flag1=False
            flag2=False
            if self.index*2+1<len(self.tree.data) and self.tree.data[self.index*2+1]!=None and self.visited[self.index*2+1]==0:
                self.index=self.index*2+1
                flag1=True
            elif self.index*2+2<len(self.tree.data) and self.tree.data[self.index*2+2]!=None and self.visited[self.index*2+2]==0:
                self.index=self.index*2+2
                flag2=True
 
        now_ele=self.tree.data[self.index]
        self.visited[self.index]=1
        self.index=(self.index+1)//2-1
        return now_ele
        
class DFSTraversalInterator_pre:
    def __init__(self,tree):
        import numpy as np
        self.tree=tree
        self.index=0
        self.visited=np.zeros(len(tree.data))
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<0:
            raise StopIteration()
        now_ele=self.tree.data[self.index]
        self.visited[self.index]=1
        while 1!=0:
            if self.index*2+1<len(self.tree.data) and self.tree.data[self.index*2+1]!=None and self.visited[self.index*2+1]==0:
                self.index=self.index*2+1
                break
            elif self.index*2+2<len(self.tree.data) and self.tree.data[self.index*2+2]!=None and self.visited[self.index*2+2]==0:
                self.index=self.index*2+2
                break
            self.index=(self.index+1)//2-1
            if self.index<0:
                break
        return now_ele
        
class DFSTraversalInterator_in:
    def __init__(self,tree):
        self.tree=tree
        self.index=0
        self.visited=np.zeros(len(tree.data))
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<0:
            raise StopIteration()
        while self.index*2+1<len(self.tree.data) and self.tree.data[self.index*2+1]!=None and self.visited[self.index*2+1]==0:
            self.index=self.index*2+1

        now_ele=self.tree.data[self.index]
        self.visited[self.index]=1
        if self.index*2+2<len(self.tree.data) and self.tree.data[self.index*2+2]!=None and self.visited[self.index*2+2]==0:
            self.index=self.index*2+2       
        else:
            while self.visited[(self.index+1)//2-1]==1 and (self.index+1)//2-1>=0:
                self.index=(self.index+1)//2-1
            self.index=(self.index+1)//2-1
        return now_ele
    
class DFSTraversal:
    def __init__(self,bt,Ttype):
        self.tree=bt
        self.type=Ttype
    def changeTraversalType(self,Ttype):
        sefl.type=Type
    def __iter__(self):
        if self.type==DFSTraversalTypes.PREORDER:
            return DFSTraversalInterator_pre(self.tree)
        if self.type==DFSTraversalTypes.INORDER:
            return DFSTraversalInterator_in(self.tree)
        if self.type==DFSTraversalTypes.POSTORDER:
            return DFSTraversalInterator_post(self.tree)