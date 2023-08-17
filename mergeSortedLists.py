from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printAll(list1: ListNode):
        currentNode = list1
        while currentNode is not None:
            print(currentNode.val)
            currentNode = currentNode.next

    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstItemSecondList = list2
        firstItemFirstList = list1
        zeroItemFirstList = list1
        while firstItemSecondList is not None:
            #take first list
            #take first item from second list
            print("A0:{} A1:{} B1:{}".format(zeroItemFirstList.val, firstItemFirstList.val, firstItemSecondList.val))

            # If we've reached the end of first list, add item to the right
            if firstItemFirstList is None:
                print ("I'm in insert to right")
                zeroItemFirstList.next = firstItemSecondList
                Solution.printAll(list1)

            #Determine whether the first item from the second list is greater than, equal to or less than 1.
            #If greater than 2 then check if its greater than the next number
            if firstItemSecondList.val > firstItemFirstList.val:
                print ("I'm changing positions")
                zeroItemFirstList = firstItemFirstList
                firstItemFirstList = firstItemFirstList.next

            #If equal to 2 then put the number on the right
            elif firstItemSecondList.val == firstItemFirstList.val: 
                print ("I'm in insert to left because equal")
                firstItemSecondList.next = firstItemFirstList
                zeroItemFirstList.next = firstItemSecondList
                firstItemSecondList = firstItemSecondList.next
                Solution.printAll(list1)
                
            #If less than 2 then put the number on the left
            elif firstItemSecondList.val < firstItemFirstList.val: 
                print ("I'm in insert to left because less than")
                firstItemSecondList.next = firstItemFirstList
                zeroItemFirstList.next = firstItemSecondList
                firstItemSecondList = firstItemSecondList.next
                Solution.printAll(list1)


list1 = ListNode(1,ListNode(3, ListNode(5,None)))
list2 = ListNode(1,ListNode(2, ListNode(4,None)))

Solution.mergeTwoLists(list1 = list1, list2 = list2)
