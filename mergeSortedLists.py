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
        
        firstItemSecondList = list2
        firstItemFirstList = list1
        zeroItemFirstList = list1
        while firstItemSecondList is not None:
            print("List 1 Item 0:{} List 1 Item 0:{} List 2 Item 1:{}".format(zeroItemFirstList.val, firstItemFirstList.val, firstItemSecondList.val))
            #take first list
            #take first item from second list
            if firstItemFirstList is None:
                print("returning none 3")
                return list2

            #Determine whether the first item from the second list is greater than, equal to or less than 1.
            #If greater than 2 then check if its greater than the next number
            if firstItemSecondList.val > firstItemFirstList.val:
                # update items and redo test
                zeroItemFirstList = firstItemFirstList
                firstItemFirstList = firstItemFirstList.next
                print ("Moving onto next")

            #If equal to 2 then put the number on the right
            elif firstItemSecondList.val == firstItemFirstList.val: 
                firstItemSecondList.next = firstItemFirstList.next
                firstItemFirstList.next = firstItemSecondList
                firstItemSecondList = firstItemSecondList.next
                print ("Inserting to the right")

            #If less than 2 then put the number on the left
            elif firstItemSecondList.val < firstItemFirstList.val: 
                zeroItemFirstList.next = firstItemSecondList
                firstItemSecondList.next = firstItemFirstList
                firstItemSecondList = firstItemSecondList.next
                print ("Inserting to the left")
            #remove from second list
            firstItemSecondList = firstItemSecondList.next
        return list1


        # Change to look back
        # Changed to use class
        # Changed to elif
        # Added null cases