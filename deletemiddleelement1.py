class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMid(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head

def createLinkedList(arr):
    head = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    return head

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
arr = list(map(int, input().split()))
head = createLinkedList(arr)
printLinkedList(head)
head = deleteMid(head)
printLinkedList(head)
