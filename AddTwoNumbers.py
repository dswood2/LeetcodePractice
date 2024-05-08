"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode() #creating linked list to be returned
        tail = new #creating linked list to be modified
        carryOne = 0 #creating switch for sum above 9
        while list1 != None or list2 != None: #are not empty
            if(list1 == None): #if list1 is empty set value to zero to continue calculation 
                list1Value = 0
            else: #get current value and move list
                list1Value = list1.val 
                list1=list1.next
            if(list2 == None): 
                list2Value = 0
            else:
                list2Value=list2.val
                list2=list2.next
            
            valueToAdd = int((list1Value+list2Value+carryOne)%10) #calculate added value
            currentNode=ListNode(valueToAdd) #create new node
            tail.next = currentNode #add to list
            tail = tail.next #move tail to previously added list     
            carryOne = int((list1Value+list2Value+carryOne)/10) #getting a carry 1 value if there is one
            
        if carryOne: #add remaining 1 if carryOne is still 1 after lists are empty
            tail.next=ListNode(1)
       
        new = new.next # move new to the final list
        return new

"""
Complexity Analysis

Time complexity : O(\max(m, n))O(max(m,n)). 
    Assume that mm and nn represents the length of l1l1 and l2l2 respectively, 
    the algorithm above iterates at most \max(m, n)max(m,n) times.

Space complexity : O(\max(m, n))O(max(m,n)). The length of the new list is at most \max(m,n) + 1max(m,n)+1.

"""