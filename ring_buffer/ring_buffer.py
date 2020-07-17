class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        num_items = 0
        oldest = None

    def append(self, item):
        if self.storage:
            if self.num_items < self.capacity:
                self.storage.append(item)
                self.num_items += 1
            else:
                self.storage[self.oldest] = item
                self.oldest += 1
                if self.oldest >= self.capacity:
                    self.oldest = 0
        else:
            self.storage.append(item)
            self.oldest = 0
            self.num_items = 1

    def get(self):
        return self.storage

# Everything runs in O(1) time!
# Displaying content of list may be O(n),
#   but that's outside this object class.