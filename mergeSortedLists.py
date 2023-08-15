# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       while list2.empty() != true:
            #take first list
            #take first item from second list
            firstItemSecondList = list2[0]
            firstItemFirstList = list1[0]
            secondItemFirstList = list1[1]
            #Determine whether the first item from the second list is greater than, equal to or less than 1.
            #If greater than 2 then check if its greater than the next number
            if firstItemSecondList > firstItemFirstList:
                if firstItemSecondList > secondItemFirstList:

            #If equal to 2 then put the number on the right
            if firstItemSecondList = firstItemFirstList: 
                list1.insert(1, firstItemSecondList)
            #If less than 2 then put the number on the left
            if firstItemSecondList < firstItemFirstList: 
                list1.insert(0, firstItemSecondList)

            #remove from second list
            list2.remove(0)

    def checkPosition(firstItemSecondList,firstItemFirstList,secondItemFirstList):
        