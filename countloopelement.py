class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
def createlinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next
    temp.next=head.next
    print(checkcycle(head))
    print(countnodesinloop(head))
def countnodesinloop(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            fast=head
            c=1
            while(True):
                if(slow==fast):
                    while(True):
                        if(slow==fast):
                            return c
                        c +=1
                        fast=fast.next
                slow=slow.next
                fast=fast.next
    return 0 
def checkcycle(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False            
arr=list(map(int,input().split()))
createlinkedlist(arr)
