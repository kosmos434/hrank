# 🌳

def insert(self, val):

    if self is None:
        return Node(val)

    if val < self.info:
        # left
        self.left = self.insert(self.left, val)
    else:
        # right
        self.right = self.insert(self.right, val)

    return self
