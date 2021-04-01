class Node():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def print_Node():
        prt = self.data
        while prt:
            print(self.data)

    def insert(self,data) :  #遞迴呼叫建立二元樹
        if self.data :      #判斷根結點在不在
            if data < self.data :  #如果新輸入資料 小於 目前節點資料
                if self.left :     #遞迴圈往下一層
                    self.left.insert(data)   #同上  在判別一次目前位置資料
                else :
                    self.left.Node(data)    #如果目前沒資料，就插入這個新資料
            else :                           #如果新輸入資料 大於目前節點資料
                if self.right :             #遞迴圈往下一層
                    self.right.insert(data)   #同上 在判別一次目前位置資料
                else:
                    self.right.Node(data)    #插入新資料
        else:
            self.data = data
h = [0]*8

y = int(input('Enter Num:'))

h.append(Node(y))
x = Node()
x.print_Node()
