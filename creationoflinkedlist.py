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
    return head  
def printlinkedlist(head):
    temp = head
    while temp:
        print(temp.val,temp.next, end=" ")
        temp = temp.next
arr = list(map(int, input().split()))
head = createlinkedlist(arr)  
printlinkedlist(head)        
