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
            print("A0:{} A1:{} B1:{}".format(zeroItemFirstList.val, firstItemFirstList.val, firstItemSecondList.val))

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
                firstItemFirstList.next = ListNode(firstItemSecondList.val, firstItemFirstList.next)

                #Look at the next one
                firstItemSecondList = firstItemSecondList.next
                firstItemFirstList = list1
                zeroItemFirstList = list1
                
                print ("Inserting to the right")
                printAll(list1)

            #If less than 2 then put the number on the left
            elif firstItemSecondList.val < firstItemFirstList.val: 
                zeroItemFirstList.next = ListNode(firstItemSecondList.val, firstItemFirstList)
                
                #Look at the next one
                firstItemSecondList = firstItemSecondList.next
                firstItemFirstList = list1
                zeroItemFirstList = list1
                
                print ("Inserting to the left")
                printAll(list1)
            #remove from second list
            
        return list1

def printAll(list1: Optional[ListNode]):
    currentNode = list1
    while currentNode is not None:
        print(currentNode.val)
        currentNode = currentNode.next