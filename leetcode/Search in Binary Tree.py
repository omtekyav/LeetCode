from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root  # Return the node if found, or None if not found
        
        if val < root.val:
            return self.searchBST(root.left, val)  # Search in the left subtree
        
        return self.searchBST(root.right, val)  # Search in the right subtree

# Example usage
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7)

val = 2
solution = Solution()
result = solution.searchBST(root, val)

# Function to print the BST in level order for visualization
def bst_to_list(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while res and res[-1] is None:
        res.pop()  # Remove trailing None values
    return res

print(bst_to_list(result))  # Output: [2, 1, 3]
