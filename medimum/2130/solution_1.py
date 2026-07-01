# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: Optional[ListNode]) -> int:
    curr = head
    next = head.next

    nums = []

    while next.next != None:
        nums.append(curr.val)
        curr = curr.next
        next = next.next.next

    nums.append(curr.val)
    curr = curr.next
    i = 0
    n = len(nums)
    answer = -1
    
    while curr != None:
        sum = curr.val + nums[n - i - 1]
        answer = max(answer, sum)
        i += 1
        curr = curr.next

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