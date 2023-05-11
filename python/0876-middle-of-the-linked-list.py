# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = self.count_nodes(head)
        middle_point = (nodes // 2) + 1
        current_node = head
        for i in range(middle_point - 1):
            current_node = current_node.next
        return current_node
    
    def count_nodes(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.count_nodes(node.next)