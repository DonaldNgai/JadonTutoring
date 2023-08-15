# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print ("hi")
        if list1 is None:
            print("returning none 1")
            return list2
        if list2 is None:
            print ("returning none 2")
            return list1
        
        # Guarunteed that either list 1 or list 2 is not null here
        sortedListHead = ListNode()
        currentListNode = sortedListHead
        currentL1Node = list1
        currentL2Node = list2
        while currentL1Node is not None and currentL2Node is not None:
            printAll(sortedListHead)
            if currentL1Node is None:
                currentListNode.val = currentL2Node.val
                currentListNode.next = currentL2Node.next
                currentL2Node = currentL2Node.next
                currentListNode = currentListNode.next
                print("L1 is empty")

            elif currentL2Node is None:
                currentListNode.val = currentL1Node.val
                currentListNode.next = currentL1Node.next
                currentL1Node = currentL1Node.next
                currentListNode = currentListNode.next
                print("L2 is empty")
            
            elif currentL1Node.val >= currentL2Node.val:
                currentListNode.val = currentL2Node.val
                currentListNode.next = currentL2Node.next
                currentL2Node = currentL2Node.next
                currentListNode = currentListNode.next
                print("L1 >= L2 ")

            elif currentL1Node.val < currentL2Node.val:
                currentListNode.val = currentL1Node.val
                currentListNode.next = currentL1Node.next
                currentL1Node = currentL1Node.next
                currentListNode = currentListNode.next
                print("L1 < L2 ")
            
        return sortedListHead

def printAll(list1: Optional[ListNode]):
    currentNode = list1
    while currentNode is not None:
        print(currentNode.val)
        currentNode = currentNode.next