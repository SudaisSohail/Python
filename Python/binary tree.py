class BTree:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.root = None
        
    def height(self):
        if self is None:
            return 0
        
        return 1 + max(BTree.height(self.left), BTree.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        
        return 1 + BTree.size(self.right) + BTree.size(self.left)
    
    def in_order(self, node):
        if node is None:
            return []
        
        return [x for x in self.in_order(node.left)] + [node.key] + [y for y in self.in_order(node.right)]
    
    def pre_order(self, node):
        if node is None:
            return []
        
        return [node.key] + [x for x in self.pre_order(node.left)] + [y for y in self.pre_order(node.right)]
    
    def post_order(self, node):
        if node is None:
            return []
        
        return [x for x in self.post_order(node.left)] + [y for y in self.post_order(node.right)] + [node.key]
    
    def traverse_sub_trees(self, node):
        if node is None:
            return []
        
        return [x for x in self.traverse_sub_trees(node.left)] + [y for y in self.traverse_sub_trees(node.right)]
        
    def display_keys(self, space='\t', level=0):
        if self is None:
            print(space * level + chr(248))
            return
        
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
        
        self.display_keys(self.right, space, level+1)
        print(space * level + str(self.key))
        self.display_keys(self.left, space, level+1)
        
    def to_tuple(self):
        if self is None:
            return None
        
        if self.left is None and self.right is None:
            return self.key
        
        return BTree.to_tuple(self.left), self.key, BTree.to_tuple(self.right)
    
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
            
        elif isinstance(data, tuple) and len(data) == 3:
            node = BTree(data[1])
            node.left = BTree.parse_tuple(data[0]) 
            node.right = BTree.parse_tuple(data[2])
            
        else:
            node = BTree(data)
            
        return node
    
    def remove_none(self, nums):
        return [x for x in nums if x is not None]
    
    def is_bst(self):
        if self is None:
            return True, None, None
        
        is_bst_l, min_l, max_l = self.is_bst(self.left)
        is_bst_r, min_r, max_r = self.is_bst(self.right)
        
        is_bst_node = (is_bst_l and is_bst_r and (max_l is None or self.key > max_l) and (min_r is None or self.key < min_r))
        
        min_key = min(self.remove_none([min_l, self.key, min_r]))
        max_key = max(self.remove_none([max_l, self.key, max_r]))
        
        return is_bst_node, min_key, max_key
    
    def list_all(self, node):
        if node is None:
            return []
        
        return [x for x in self.list_all(node.left)] + [node.key] + [y for y in self.list_all(node.right)]
    
    def insert(self, node, key, value):
        if node is None:
            node = BTree(key, value)
        
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
            node.left.parent = node
            
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
            node.right.parent = node
            
        return node
    
    def find(self, node, key):
        if node is None:
            return None
        
        if key == node.key:
            return node
        
        if key < node.key:
            return self.find(node.left, key)
        
        if key > node.key:
            return self.find(node.right, key)           
        
    def update(self, node, key, value):
        target = self.find(node, key)
        
        if target is not None:
            target.value = value
            
    def is_balanced(self, node):
        if node is None:
            return True, 0
        
        balanced_l, height_l = self.is_balanced(node.left)
        balanced_r, height_r = self.is_balanced(node.right)
            
        balanced = balanced_l and balanced_r and abs(height_l - height_r)
        height = 1 + max(height_l, height_r)
        
        return balanced, height
    
    @staticmethod
    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
            
        if lo > hi:
            return None
        
        mid = (lo + hi) // 2 if len(data) > 2 else 1
        print("Mid is", mid, "\n\n")
        key = data[mid]
        
        root = BTree(key)
        root.parent = parent
        root.left = BTree.make_balanced_bst(data, lo, mid-1, root)
        root.right = BTree.make_balanced_bst(data, mid+1, hi, root)
        
        return root
    
    def balance_bst(self):
        print(self.list_all(self.root))
        return self.make_balanced_bst(self.list_all(self))
    
    def __str__(self):
        return f"BinaryTree <{self.to_tuple()}>"
    
    def __repr__(self):
        return f"BinaryTree <{self.to_tuple()}>"
    
    def __setitem__(self, key, value):
        node = self.find(self, key)
        
        if not node:
            self.root = self.insert(self, key, value)
            self.root = self.balance_bst()
            
        else:
            self.update(self, key, value)
            
    def __getitem__(self, key):
        node = self.find(self, key)
        return node.value if node else None
    
    def __delitem__(self, node, key):
        
        if node.key == key:
            node = None
            
        else:
            t_node = self.find(node, key)
            
        sub_tree = self.list_all((x for x in self.traverse_sub_trees(t_node) if x is not None))
        
        return self.make_balanced_bst(sub_tree)   
    
    def __iter__(self):
        return (x for x in self.list_all(self.root))
    
    def __len__(self):
        return self.size()
    
    def display(self):
        return self.display_keys()
    
"""Tree = BTree("Sudais", "Sudais Ahmed")

Tree["Ibrahim"] = "MIthai ka dabba"
Tree["Sarah"] = "Chapati"
Tree["Muhammad"] = "Minecraft ka deewana"
Tree["Ali"] = "Climber"
Tree["Izzah"] = "Sust"
Tree["Shifa"] = "Pareshan"

Tree.display()         
        
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))"""

lst = [1, 6, 7, 14, 29, 45, 46, 73, 100]
tree = BTree.make_balanced_bst(lst)
print(type(tree))

tree.display_keys()
