class Node:
    def _init_(self,data):
        self.prev=None
        self.val=data
        self.next=None
def createcircularlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            newNode=Node(data)
            temp.next=newNode
            newNode.prev=temp
            temp=temp.next
            temp.next=head
            head.prev=temp
    printcircularlist(head)
def printcircularlist(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next
arr=list(map(int,input().split()))
createcircularlist(arr)