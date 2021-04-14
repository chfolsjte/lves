

a =[9,2,6,1,11,8,3,18,20,5]    #建立串列 a


class Node():                    #定義 節點

    def __init__(self,data=None):       #self必要，data預設為None
        self.data = data
        self.right = None
        self.left = None

class buildTree():

    def insert(self,data) :  #遞迴呼叫建立二元樹
        if self.data :       #判斷根結點在不在
            print(self.data)
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
        else :                                 #如果跟節點不在，建立根結點
            self.data = data               #建立 新資料 為節點
            print(self.data)
x = Node()
tree=[]
for i in a:
    x.insert(i)
tree.append(x)
