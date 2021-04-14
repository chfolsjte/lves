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

        if self.left:
            self.left.pporder()
        if self.right:
            self.right.pporder()
        print(self.data)


class POST():
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root1 = Node(preorder[0])
        index = inorder.index(root1.data)
        root1.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
        root1.right = self.buildTree(preorder[index + 1 : ], inorder[index + 1 :])
        tree1.append(root1.data)
        return root1
class PRE():
    def buildTree(self, postorder, inorder):
        if len(postorder) == 0:
            return None
        root = Node(postorder[-1])
        #print(tree)
        index = inorder.index(root.data)  #8
        tree.append(root.data)
        root.left = self.buildTree(postorder[ :index ], inorder[:index])

        root.right = self.buildTree(postorder[index: -1], inorder[index+1:])

        return root

tree = []
tree1=[]
tree2=[]
tree4=[]
#inorder = [9,3,15,20,7]
#preorder = [3,9,20,15,7]
#xxx = [10,21,5,9,13,28]
#中序  先處理最左子點  在處理父節點  在處理右子點
TY = [10,21,5,9,13,28]
inorder = ['C','B','E','D','F','N','J','X',   'A',  'G','I','H','Y','L','K','M','Z']

postorder = ['C', 'E', 'N', 'X', 'J', 'F', 'D',     'B',     'I', 'Y', 'L', 'Z', 'M', 'K', 'H', 'G', 'A']
#前序  經過的節點都處理，往左下走，再往右下
preorder = ['A','B','C','D','E','F','J','N','X','G','H','I','K','L','Y','M','Z',]
j = Node()
po  = POST()
x = po.buildTree(preorder,inorder)
pr = PRE()
x1 = pr.buildTree(postorder,inorder)
#print(tree)
#print(tree1)
#for i in postorder :
#    j.insert(i)
#tree2.append(j)
#print(x.right.data)
for i in TY:
    j.insert(i)

j.pporder()
tree4.append(j)
print('tree=',tree4[0].data)
