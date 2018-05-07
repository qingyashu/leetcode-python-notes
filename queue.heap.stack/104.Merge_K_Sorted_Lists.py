from heapq import heappush, heappop
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    # heap solution
    def mergeKLists1(self, lists):
        hp = []
        for head in lists:
            if head:
                heappush(hp, (head.val, head))
        dum = ListNode(0)
        ptr = dum
        while hp:
            v, p = heappop(hp)
            node = p
            p = p.next
            node.next = None
            ptr.next = node
            ptr = ptr.next
            if p:
                heappush(hp, (p.val, p))
        return dum.next

    # divided and conquer solution
    def mergeKLists2(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) > 2:
            n1 = len(lists) / 2
            n2 = len(lists) - n1
            l1 = self.mergeKLists(lists[0:n1])
            l2 = self.mergeKLists(lists[n1:])
            return self.mergeKLists([l1, l2])
        if len(lists) == 2:
            if lists[0] is None:
                return lists[1]
            if lists[1] is None:
                return lists[0]
            p1 = lists[0]
            p2 = lists[1]
            dum = ListNode(0)
            cur = dum
            while p1 or p2:
                if p1 is None:
                    cur.next = p2
                    cur = cur.next
                    p2 = p2.next
                elif p2 is None:
                    cur.next = p1
                    cur = cur.next
                    p1 = p1.next
                elif p1.val < p2.val:
                    cur.next = p1
                    cur = cur.next
                    p1 = p1.next
                else:
                    cur.next = p2
                    cur = cur.next
                    p2 = p2.next
            return dum.next
                    