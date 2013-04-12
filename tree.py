class Tree():
    
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
    
    def is_leaf(self):
        return self.right is None and self.left is None
    
    def preorder(self):
        s = self.value + '\n'
        if self.left:
            s += self.left.preorder()
        if self.right:
            s += self.right.preorder()
        return s
    
    def nodes_dict(self):
        nodes = {self: self.value}
        if self.left:
            nodes.update(self.left.nodes_dict())
        if self.right:
            nodes.update(self.right.nodes_dict())
        return nodes
    
    def graphviz_id(self, i):
        return 'node_%s' % str(i) if i >= 0 else '_'+str(-i)
    
    def graphviz_nodes(self, i=0):
        s = '%s [label=%s]\n' % (self.graphviz_id(i), self.value)
        if self.left:
            s += self.left.graphviz_nodes(i + 1)
        if self.right:
            s += self.right.graphviz_nodes(i - 1)
        return s
    
    def graphviz_edges(self, i=0):
        s = ''
        if self.left:
            s += '%s -> %s\n' % (self.graphviz_id(i), self.left.graphviz_id(i + 1))
            s += self.left.graphviz_edges(i + 1)
        if self.right:
            s += '%s -> %s\n' % (self.graphviz_id(i), self.right.graphviz_id(i - 1))
            s += self.right.graphviz_edges(i - 1)
        return s
    
    def __unicode__(self):
        return self.preorder()

def read_tree(filename):
    stack = []
    for line in open(filename):
        vals = line.split(' ')
        t = Tree(vals[0])
        if vals[1] == '1':
            t.right = stack.pop()
        if vals[2] == '1':
            t.left = stack.pop()
        stack.append(t)
    return stack.pop()

def to_graphviz(tree):
    nodes = tree.nodes_dict()
    s = 'digraph {\n'
    s += tree.graphviz_nodes()
    s += tree.graphviz_edges()
    # s += '\n'.join(['\tnode%d [label=%s]' % (x, label) for x, label in zip(xrange(len(nodes)), nodes.values())])
    s += '\n}'
    return s

print(to_graphviz(read_tree('treetest')))
