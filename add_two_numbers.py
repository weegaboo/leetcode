# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9],
#        l2 = [9,9,9,9]
# Output:     [8,9,9,9,0,0,0,1]
#
#
# Constraints:
# - The number of nodes in each linked list is in the range [1, 100].
# - 0 <= Node.val <= 9
# - It is guaranteed that the list represents a number that does not have leading zeros.


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None
        result = ListNode()
        current = result
        remainder = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                first_num = l1.val
                l1 = l1.next
            else:
                first_num = 0

            if l2 is not None:
                second_num = l2.val
                l2 = l2.next
            else:
                second_num = 0

            sum_val = first_num + second_num + remainder
            remainder = sum_val // 10
            current.val = sum_val % 10
            if l1 is not None or l2 is not None:
                current.next = ListNode()
                current = current.next
        if remainder != 0:
            current.next = ListNode(val=remainder)
        return result


if __name__ == "__main__":
    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))))
    l2 = ListNode(val=9, next=ListNode(val=9))
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result is not None:
        print(result.val)
        result = result.next