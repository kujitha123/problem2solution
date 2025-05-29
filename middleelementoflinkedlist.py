class Node:
    def __init__(self, data):  
        self.val = data
        self.next = None
def createlinkedlist(arr):
    head = None
    temp = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    middleNode=getmiddle(head)  
def getmiddle(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    return slow.val
arr=list(map(int,input().split()))
print(createlinkedlist(arr))
