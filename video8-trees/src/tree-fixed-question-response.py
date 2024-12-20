
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        # insert a key,value pair
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.root.insert(key, value)

    def lookup(self, key):
        # lookup value by key
        if self.root is	None:
            return None
        else:
            node = self.root.find(key)
            if node is None:
                return None
            else:
                return node.value

    def delete(self, key):
        # delete by key
        if self.root is None:
            raise KeyError
        else:
            self.root = self.root.delete(key)

    def walk(self):
        if self.root is None:
            return
        yield from self.root.walk()
    
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value):
        if key < self.key:
            # left
            if self.left is None:
                n = TreeNode(key, value)
                self.left = n
            else:
                self.left.insert(key, value)
        else:
            # right
            if self.right is None:
                n = TreeNode(key, value)
                self.right = n
            else:
                self.right.insert(key, value)

    def find(self, key):
        if key == self.key:
            return self
        if key < self.key:
            # left
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        else:
            # right
            if self.right is None:
                return None
            else:
                return self.right.find(key)

    def maxkey(self):
        if self.right is None:
            return self.key
        return self.right.maxkey()

    def delete(self, key):
        if self.key == key:
            # delete this node
            if self.left is None and self.right is None:
                # we have no children
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                # Find the maximum node in the left subtree
                maxkey = self.left.maxkey()
                maxnode = self.left.find(maxkey)
                # Replace the value of the current node with the maximum node's value
                self.key = maxnode.key
                self.value = maxnode.value
                # Delete the maximum node
                self.left = self.left.delete(maxkey)
                return self
                
        elif key < self.key:
            # ask left child to delete
            if self.left is None:
                raise KeyError
            self.left = self.left.delete(key)
        else:
            # ask right child to delete
            if self.right is None:
                raise KeyError
            self.right = self.right.delete(key)            
        return self

    def walk(self):
        if self.left is not None:
            yield from self.left.walk()
        yield (self.key, self.value)
        if self.right is not None:
            yield from self.right.walk()
    

def test_add_find():
    tn = TreeNode(10, "ten")
    tn.insert(5, "five")
    tn.insert(15, "fifteen")
    node = tn.find(5)
    assert(node.key == 5)
    assert(node.value == "five")

    node = tn.find(15)
    assert(node.key == 15)
    assert(node.value == "fifteen")

    assert(tn.maxkey() == 15)
    assert(tn.key == 10)
    tn = tn.delete(10)
    assert(tn.key == 5)

    tn = tn.delete(15)
    assert(tn.key == 5)
    assert(tn.maxkey() == 5)

    tn = tn.delete(5)
    assert(tn is None)

def test_tree():
    t = BinaryTree()
    v = t.lookup(1)
    assert(v is None)
    t.insert(10, "10")
    t.insert(5, "5")
    t.insert(15, "15")
    assert(t.lookup(10) == "10")
    assert(t.lookup(5) == "5")
    assert(t.lookup(15) == "15")
    
    t.delete(10)
    assert(t.lookup(10) is None)
    assert(t.lookup(5) == "5")
    assert(t.lookup(15) == "15")

    t.delete(5)
    assert(t.lookup(10) is None)
    assert(t.lookup(5) is None)
    assert(t.lookup(15) == "15")

    t.delete(15)
    assert(t.lookup(10) is None)
    assert(t.lookup(5) is None)
    assert(t.lookup(15) is None)
    
def test_walk():
    items = [(10,10), (5,5), (15,15), (12,12), (1,1), (6,6)]
    t = BinaryTree()
    for k,v in items:
        t.insert(k, v)

    items.sort()
    extracted = []
    for k,v in t.walk():
        extracted.append((k,v))
    assert(extracted == items)

def test_delete():
    items = [(10,10), (5,5), (15,15), (12,12), (1,1), (6,6)]
    t = BinaryTree()
    for k,v in items:
        t.insert(k, v)

    t.delete(5)

    raised = False
    try:
        t.delete(7)
    except KeyError:
        raised = True
    assert(raised)

    t.delete(10)

    raised = False
    try:
        t.delete(10)
    except KeyError:
        raised = True
    assert(raised)

    t.delete(15)
    t.delete(12)
    t.delete(1)
    t.delete(6)
    for i in t.walk():
        assert(False)

    raised = False
    try:
        t.delete(6)
    except KeyError:
        raised = True
    assert(raised)




