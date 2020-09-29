# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
포인터는 총 3개가 필요함.

tmp : 링크를 변경하고 다음 노드로 이동하기 위한 포인터
cur : 링크를 변경시킬 현재 노드의 포인터
prev : cur의 링크가 가리킬 이전 노드의 포인터

A -> B -> C -> D -> E

head가 곧 tail이 되어야 하므로 prev가 head를 가리키도록 한 다음 head.next = None 으로 업데이트.
tmp = C, cur = B, prev = A

cur.next = prev ==> A(prev) <- B(cur)        C(tmp)      -> D -> E
prev = cur      ==> A       <- B(prev, cur)  C(tmp)      -> D -> E
cur = tmp       ==> A       <- B(prev)       C(cur, tmp) -> D -> E
tmp = cur.next  ==> A       <- B(prev)       C(cur)      -> D(tmp) -> E
 
cur.next = prev ==> A       <- B(prev)    <- C(cur)         D(tmp)      -> E
prev = cur      ==> A       <- B          <- C(prev, cur)   D(tmp)      -> E
cur = tmp       ==> A       <- B          <- C(prev)        D(cur, tmp) -> E
tmp = cur.next  ==> A       <- B          <- C(prev)        D(cur)      -> E(tmp)
'''

class Solution:
    def reverseList(self, head):
        if not head:
            return None

        prev = head
        cur = head.next
        prev.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev


'''
포인터 2개를 이용한 솔루션
'''
class SolutionWith2pointer:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
