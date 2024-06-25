class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildBST(preorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    left_preorder = [x for x in preorder if x < root_val]
    right_preorder = [x for x in preorder if x > root_val]
    root.left = buildBST(left_preorder)
    root.right = buildBST(right_preorder)
    return root

def postorderTraversal(root):
    if not root:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]

if __name__ == "__main__":
    n = int(input())
    preorder = list(map(int, input().split()))
    root = buildBST(preorder)
    result = postorderTraversal(root)
    print(' '.join(map(str, result)))
