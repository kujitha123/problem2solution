class Node:
    def __init__(self,data):
        self.left=None
        self.val=data
        self.right=None
def createBST(arr):
    root=None
    for data in arr:
        if(root==None):
            root=Node(data)
        else:
            temp=root
            while(True):
                #smaller elements
                if(data<temp.val):
                    if(temp.left==None):
                        temp.left=Node(data)
                        break
                    else:
                        temp=temp.left
                #larger elements
                if(data>temp.val):
                    if(temp.right==None):
                        temp.right=Node(data)
                        break
                    else:
                        temp=temp.right
    inorder(root)
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
    
    preorder(root)
def preorder(root):
    if(root==None):
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)
    
    postorder(root)
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")

    #print(root.left.right.val)
arr=list(map(int,input().split()))
createBST(arr)


            
                
                
    
