class Node:
    def _init_(self,data):
        self.val=data
        self.next=None
def createlinkedlist(arr):#to create linked list
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next
    printlinkedlist(head)

def printlinkedlist(head):## to print the linked list
    temp=head
    while(temp):
        print(temp.val,temp.next,end=" ")
        temp=temp.next
arr=list(map(int,input().split()))
createlinkedlist(arr)