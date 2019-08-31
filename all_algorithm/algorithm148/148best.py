# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#链表排序，归并排序。哈哈哈让我们来试试




class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.

        '''
        首先必须要找到中点，才能够。进去递归。把前，中部分，递归。 再把中，后部分，递归。
        
        然后就是两个有序链表合并的故事了。是的。
        '''
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


