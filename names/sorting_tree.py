class BSTNode:
    # No duplicates!
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def compare(self, a, b):
        # compares strings in alphabetical order
        # returns -1 if a is first, 1 if b is first, 0 if same
        if not (isinstance(a, str) and isinstance(b, str)):
            return None
        if ord(a[0]) < ord(b[0]):
            return 1
        if ord(a[0]) > ord(b[0]):
            return -1
        if ord(a[0]) == ord(b[0]):
            if len(a) > 1 and len(b) > 1:
                return self.compare(a[1:], b[1:])
            if len(a) == 1 and len(b) == 1:
                return 0
            if len(a) == 1 and len(b) > 1:
                return 1
            if len(a) > 1 and len(b) == 1:
                return -1

    def insert(self, value):
        if not self.value:
            self.value = value
            return None
        comp = self.compare(value, self.value)
        if comp == -1:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
                return None
        if comp == 1:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return None
        if comp == 0:
            return None
    
    def contains(self, target):
        comp = self.compare(target, self.value)
        if target == self.value:
            return True
        elif comp == -1:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif comp == 1:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return False

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)