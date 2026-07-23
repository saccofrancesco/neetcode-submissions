class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy boundary nodes
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node) -> None:
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous

    def _insert_most_recent(self, node: Node) -> None:
        previous = self.right.prev

        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Accessing the node makes it the most recently used
        self._remove(node)
        self._insert_most_recent(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._insert_most_recent(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert_most_recent(node)

        if len(self.cache) > self.capacity:
            least_recent = self.left.next

            self._remove(least_recent)
            del self.cache[least_recent.key]