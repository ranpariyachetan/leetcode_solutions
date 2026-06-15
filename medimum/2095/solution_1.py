# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next= None):
        self.val = val
        self.next = next

def getMiddleNode(head: ListNode):
    prev = ListNode(-1, head)
    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        prev = prev.next
        slow = slow.next
        fast = fast.next.next

    return prev, slow


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:

    if head == None or head.next == None:
        return None

    prev = ListNode(-1, head)
    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        prev = prev.next
        slow = slow.next
        fast = fast.next.next

    if fast == None:
        prev.next = slow.next
    else:
        slow.next = slow.next.next

    return head


def getMiddleNode(head: ListNode):
    prev = ListNode(-1, head)
    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        prev = prev.next
        slow = slow.next
        fast = fast.next.next

    if fast == None:
        print(f"Fast is None: {fast == None}")
    else:
        print(f"Fast.next is None: {fast.next == None}")
    return prev, slow

def buildLinkedList(vals) -> ListNode:
    head = ListNode()
    temp = head

    for val in vals:
        temp.next = ListNode(val)
        temp = temp.next

    return head.next

def displayLinkedList(head):
    output = ""
    while head != None:
        output += f"{head.val} --> "
        head = head.next

    output = str.rstrip(output, " --> ")

    print(output)


head = buildLinkedList([1,3,4,7,1,2,6])
displayLinkedList(head)
newHead = deleteMiddle(head)
displayLinkedList(newHead)

print("-" * 30)

head = buildLinkedList([1,3,4,5,1,2])
displayLinkedList(head)
newHead = deleteMiddle(head)
displayLinkedList(newHead)
print("-" * 30)

head = buildLinkedList([1,2,3,4])
displayLinkedList(head)
newHead = deleteMiddle(head)
displayLinkedList(newHead)
print("-" * 30)

head = buildLinkedList([2,1])
displayLinkedList(head)
newHead = deleteMiddle(head)
displayLinkedList(newHead)
print("-" * 30)


head = buildLinkedList([2,1,3])
displayLinkedList(head)
newHead = deleteMiddle(head)
displayLinkedList(newHead)
print("-" * 30)