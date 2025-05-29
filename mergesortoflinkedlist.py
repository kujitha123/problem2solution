class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSort(head):
    if not head or not head.next:
        return head
    middle = getMiddle(head)
    right = middle.next
    middle.next = None
    left_sorted = mergeSort(head)
    right_sorted = mergeSort(right)
    return merge(left_sorted, right_sorted)

def getMiddle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2):
    temp = Node(0)
    tail = temp
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return temp.next

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
head=createLinkedList(arr)
sorted_head = mergeSort(head)
printLinkedList(sorted_head)
