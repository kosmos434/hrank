# 🌳

def height(root):
    if not root:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        return max(left, right) + 1
