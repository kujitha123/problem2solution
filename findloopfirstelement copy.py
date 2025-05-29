class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def createlinkedlist(arr):
    head = None
    temp = None
    for data in arr:
        new_node = Node(data)
        if head is None:
            head = new_node
            temp = head
        else:
            temp.next = new_node
            temp = temp.next

    if head and head.next:
        temp.next = head.next 

    start_node = findCycleStart(head)
    if start_node:
        print(start_node.val)
    else:
        print("No cycle detected")

def findCycleStart(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

arr = list(map(int, input().split()))
createlinkedlist(arr)
