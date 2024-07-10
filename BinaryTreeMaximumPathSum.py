'''
A path in a binary tree is a sequence of nodes where each pair of 
adjacent nodes in the sequence has an edge connecting them. A node 
can only appear in the sequence at most once. Note that the path does 
not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum 
of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
* The number of nodes in the tree is in the range [1, 3 * 10^4].
* -1000 <= Node.val <= 1000
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Recursively find the maximum path sum for left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Calculate the maximum path sum that includes the current node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum sum if necessary
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain for the parent call
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

# Example usage
if __name__ == "__main__":
    # Create the tree from Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    # Create the tree from Example 2
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)

    solution = Solution()
    print("Example 1 output:", solution.maxPathSum(root1))  # Expected: 6
    print("Example 2 output:", solution.maxPathSum(root2))  # Expected: 42



'''
Example:

       -10
       /  \
      9    20
          /  \
         15   7

Let's step through the `max_gain` function for each node:

1. We start at the root (-10):
   max_gain(-10)
   
2. We first process the left child (9):
   max_gain(9)
   
   - It has no children, so left_gain and right_gain are both 0
   - current_path_sum = 9 + 0 + 0 = 9
   - self.max_sum is updated to 9
   - Returns 9

3. We then process the right child (20):
   max_gain(20)
   - We need to process its children first

4. Processing 15:
   max_gain(15)
   
   - No children, so left_gain and right_gain are 0
   - current_path_sum = 15 + 0 + 0 = 15
   - self.max_sum is updated to 15
   - Returns 15

5. Processing 7:
   max_gain(7)
   
   - No children, so left_gain and right_gain are 0
   - current_path_sum = 7 + 0 + 0 = 7
   - self.max_sum remains 15
   - Returns 7

6. Back to processing 20:
   - left_gain = max(15, 0) = 15
   - right_gain = max(7, 0) = 7
   - current_path_sum = 20 + 15 + 7 = 42
   - self.max_sum is updated to 42
   - Returns 20 + max(15, 7) = 35

7. Finally, back to the root (-10):
   - left_gain = max(9, 0) = 9
   - right_gain = max(35, 0) = 35
   - current_path_sum = -10 + 9 + 35 = 34
   - self.max_sum remains 42
   - Returns -10 + max(9, 35) = 25

The algorithm returns 42 as the maximum path sum, which corresponds 
to the path 15 -> 20 -> 7.

Key points to note:
1. At each node, we calculate the max path sum that includes that node 
   and both its subtrees (current_path_sum).
2. We update our global max (self.max_sum) if this new path sum is larger.
3. We return the max path sum that starts at this node and goes down 
   one subtree, which allows our parent to potentially use us in a 
   larger path.

This process allows us to consider all possible paths in the tree, not 
just those that go through the root, and find the one with the maximum sum.

'''