# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next= None):
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:

    if head.next == None:
        return None

    slow = head
    fast = head.next.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    slow.next = slow.next.next

    return head


def buildLinkedList(vals) -> ListNode:
    head = ListNode()
    temp = head

    for val in vals:
        temp.next = ListNode(val)
        temp = temp.next

    return head.next

def displayLinkedList(head):
    output = ""

    temp = head
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