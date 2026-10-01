# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Map values to their indices in inorder array for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_idx: int, right_idx: int) -> TreeNode | None:
            nonlocal pre_idx
            
            # Base case: no elements in the current subtree
            if left_idx > right_idx:
                return None

            # Pick current root from preorder array
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Root splits inorder array into left and right subtrees
            inorder_split = inorder_map[root_val]

            # Build left subtree then right subtree
            root.left = helper(left_idx, inorder_split - 1)
            root.right = helper(inorder_split + 1, right_idx)

            return root

        return helper(0, len(inorder) - 1)