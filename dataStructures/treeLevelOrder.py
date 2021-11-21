# 🌳

# use a queue instead of recursion
def levelOrder(root):
    queue = [root]

    while len(queue) > 0:
        current = queue[0]
        print(current, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        queue.pop(0)
