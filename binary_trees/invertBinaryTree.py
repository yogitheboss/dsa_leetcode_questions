#INVERT BINARY TREE

# Given the root of a binary tree, invert the tree, and return its root.
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]


#problem link:https://leetcode.com/problems/invert-binary-tree/description/


#Solution:


def invertTree( root):
        helper(root)
        return root

        
def helper(root):
        if(root==None):
            return

#swapping left and right pointers
        temp=root.left
        root.left=root.right
        root.right=temp

        # or         root.left,root.right=root.right,root.left

        helper(root.left)
        helper(root.right)
