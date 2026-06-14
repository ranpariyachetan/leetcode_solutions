# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: Optional[ListNode]) -> int:
    answer = -1
    left = head

    def dfs(right):
        nonlocal answer, left
        if right.next != None:
            dfs(right.next)

        answer = max(answer, left.val + right.val)
        left = left.next

    dfs(head)
    return answer

def buildLinkedList(vals) -> ListNode:
    head = ListNode()
    temp = head

    for val in vals:
        temp.next = ListNode(val)
        temp = temp.next

    return head.next

head = buildLinkedList([5,4,2,1])
print(pairSum(head))

head = buildLinkedList([4,8,11,1,2,3])
print(pairSum(head))

head = buildLinkedList([1, 100000])
print(pairSum(head))