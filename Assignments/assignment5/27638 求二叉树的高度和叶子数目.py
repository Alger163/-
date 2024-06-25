class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(nodes):
    if not nodes:
        return None
    tree = [TreeNode(i) for i in range(len(nodes))]
    for i, (left, right) in enumerate(nodes):
        if left != -1:
            tree[i].left = tree[left]
        if right != -1:
            tree[i].right = tree[right]
    return tree[0]


def tree_height_and_leaves(root):
    if not root:
        return 0, 0

    stack = [(root, 1)]
    max_height = 0
    leaves_count = 0

    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)

        if not node.left and not node.right:
            leaves_count += 1

        if node.left:
            stack.append((node.left, height + 1))
        if node.right:
            stack.append((node.right, height + 1))

    return max_height, leaves_count+1


# 读取输入
n = int(input())
nodes = [tuple(map(int, input().split())) for _ in range(n)]

# 构建二叉树
root = build_tree(nodes)

# 计算二叉树高度和叶子节点个数
height, leaves = tree_height_and_leaves(root)

# 输出结果
print(height, leaves)
