class Node:
    def __init__(self,data):
        self.prev=None
        self.val=data
        self.next=None
def createdoublylinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            newNode=Node(data)
            newNode.prev=temp
            temp.next=newNodew
            temp=temp.next
    print(doublylinkedlist(head))
    print(deletehead(head))
def deletehead(head):
    temp=head.next
    head.next=None
    return temp
def printdoublylinkedlist(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next   
arr=list(map(int,input().split()))
createdoublylinkedlist(arr)
deletehead(head)
            
