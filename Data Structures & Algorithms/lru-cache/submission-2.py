class Node:
    def __init__(self, key, value):

        # Store key because when we remove a node
        # from the linked list, we also need to
        # remove the same key from the hashmap.
        self.key = key

        # Actual value associated with the key.
        self.value = value

        # Previous pointer in Doubly Linked List.
        self.prev = None

        # Next pointer in Doubly Linked List.
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        # Maximum number of items allowed in cache.
        self.capacity = capacity

        # -------------------------------------------------
        # HashMap
        #
        # key  ---> corresponding node
        #
        # Example:
        #
        # 5 ---> Node(5,100)
        #
        # This lets us find any node in O(1).
        # -------------------------------------------------
        self.cache = {}

        # -------------------------------------------------
        # Create two dummy nodes.
        #
        # left  = Dummy node before LRU
        # right = Dummy node after MRU
        #
        # Initially:
        #
        # left <------> right
        #
        # No real nodes yet.
        # -------------------------------------------------
        self.left = Node(0, 0)     # LRU Dummy
        self.right = Node(0, 0)    # MRU Dummy

        # Connect dummy nodes together.
        self.left.next = self.right
        self.right.prev = self.left

    # =====================================================
    # REMOVE A NODE
    #
    # Before:
    #
    # A <-> B <-> C
    #
    # remove(B)
    #
    # After:
    #
    # A <-> C
    # =====================================================
    def remove(self, node):

        # Save neighbours.
        previous = node.prev
        nxt = node.next

        # Skip the current node.
        previous.next = nxt
        nxt.prev = previous

    # =====================================================
    # INSERT NODE AT END
    #
    # We always insert just before right dummy.
    #
    # Before:
    #
    # left <-> A <-> B <-> right
    #
    # insert(C)
    #
    # After:
    #
    # left <-> A <-> B <-> C <-> right
    #
    # C becomes Most Recently Used.
    # =====================================================
    def insert(self, node):

        # Last real node before right dummy.
        previous = self.right.prev

        # Connect previous node to new node.
        previous.next = node
        node.prev = previous

        # Connect new node to right dummy.
        node.next = self.right
        self.right.prev = node

    # =====================================================
    # GET
    #
    # If key exists:
    #
    # 1. Move node to MRU position.
    # 2. Return value.
    #
    # Else return -1.
    # =====================================================
    def get(self, key: int) -> int:

        # Key not present.
        if key not in self.cache:
            return -1

        # Get corresponding node.
        node = self.cache[key]

        # Since this key was accessed,
        # it becomes Most Recently Used.
        self.remove(node)
        self.insert(node)

        # Return stored value.
        return node.value

    # =====================================================
    # PUT
    #
    # Insert new key/value pair.
    #
    # If key already exists:
    # remove old node first.
    #
    # If capacity exceeds:
    # remove Least Recently Used node.
    # =====================================================
    def put(self, key: int, value: int) -> None:

        # -----------------------------------------
        # Key already exists.
        #
        # Remove old version from linked list
        # and hashmap.
        # -----------------------------------------
        if key in self.cache:

            self.remove(self.cache[key])
            del self.cache[key]

        # -----------------------------------------
        # Create brand new node.
        # -----------------------------------------
        node = Node(key, value)

        # Store in hashmap.
        self.cache[key] = node

        # Insert at MRU position
        # (just before right dummy).
        self.insert(node)

        # -----------------------------------------
        # Cache exceeded capacity.
        #
        # Remove Least Recently Used node.
        # -----------------------------------------
        if len(self.cache) > self.capacity:

            # First real node after left dummy
            # is always Least Recently Used.
            lru = self.left.next

            # Remove from linked list.
            self.remove(lru)

            # Remove from hashmap.
            del self.cache[lru.key]