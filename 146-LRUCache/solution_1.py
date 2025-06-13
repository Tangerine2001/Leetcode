class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

    def __repr__(self):
        res = f'{self.val}'

        prev = self.prev
        while prev:
            res = f'{prev.val}<-{res}'
            prev = prev.prev

        nxt = self.nxt
        while nxt:
            res = f'{res}->{nxt.val}'
            nxt = nxt.nxt
        return res


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = dict()
        self.start, self.end = Node(0, 0), Node(0, 0)
        self.start.nxt = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if not (node := self.cache.get(key)):
            return -1
        self.remove(node)
        self.move_to_end(node)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if (node := self.cache.get(key)):
            self.remove(node)
            self.count -= 1

        self.cache[key] = Node(key, value)
        self.move_to_end(self.cache[key])
        self.count += 1

        if self.count > self.capacity:
            # cannot add a new one, too many
            node = self.start.nxt
            self.remove(node)
            del self.cache[node.key]
            self.count -= 1

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def move_to_end(self, node):
        prev, nxt = self.end.prev, self.end
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev, nxt