'''
class node() :
    def __init__(self,date=None):
        self.date = date
        self.next = None

class Linked_list():
    def node_head(self,date=None):
        self.head = date
        self.next = None




n1 = node(5)
n2 = node(10)
n3 = node(3)

n1.next = n2
n2.next = n3


ptr = n1

while ptr :

    print(ptr.date)
    ptr = ptr.next
'''
class Node():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def print_Node(self):

        print(self.data)

    def insert(self,data) :  #遞迴呼叫建立二元樹
        if self.data :      #判斷根結點在不在
            if data < self.data :  #如果新輸入資料 小於 目前節點資料
                if self.left :     #遞迴圈往下一層
                    self.left.insert(data)   #同上  在判別一次目前位置資料
                else :
                    self.left = Node(data)    #如果目前沒資料，就插入這個新資料
            else :                           #如果新輸入資料 大於目前節點資料
                if self.right :             #遞迴圈往下一層
                    self.right.insert(data)   #同上 在判別一次目前位置資料
                else:
                    self.right = Node(data)    #插入新資料
        else:
            self.data = data

    def inorder(self) :
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self) :

        print(self.data)
        if self.left :
            self.left.preorder()
        if self.right :
            self.right.preorder()

    def pporder(self) :

        if self.right:
            self.right.inorder()
        print(self.data)
        if self.left:
            self.left.inorder()


class Solution():
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = Node(preorder[0])
        #print(root.data)
        index = inorder.index(root.data) # 中序中根节点的位置，左边即为左子树，右边由子树
        root.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
        root.right = self.buildTree(preorder[index + 1 : ], inorder[index + 1 :])

        print(root.data)

tree = Node()
#inorder = [9,3,15,20,7]
#preorder = [3,9,20,15,7]
#xxx = [10,21,5,9,13,28]
P = ['C','E','N','X','J','F','D','B','I','Y','L','Z','M','K','H','G','A']
for i in P:
    tree.insert(i)
tree.preorder()
#中序  先處理最左子點  在處理父節點  在處理右子點
inorder = ['C','B','E','D','F','N','J','X','A','G','I','H','Y','L','K','M','Z',]
#前序  經過的節點都處理，往左下走，再往右下
preorder = ['A','B','C','D','E','F','J','N','X','G','H','I','K','L','Y','M','Z',]


SO  = Solution()
x = SO.buildTree(preorder,inorder)
