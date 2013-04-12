class Tree():
    'Minimal binary tree class for testing.'
    
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
    
    def is_leaf(self):
        'A leaf has no children on right or left.'
        return self.right is None and self.left is None
    
    def preorder(self):
        'Returns a string representing this tree as a preorder traversal.'
        s = self.value + '\n'
        if self.left:
            s += self.left.preorder()
        if self.right:
            s += self.right.preorder()
        return s
    
    # def nodes_dict(self):
    #     nodes = {self: self.value}
    #     if self.left:
    #         nodes.update(self.left.nodes_dict())
    #     if self.right:
    #         nodes.update(self.right.nodes_dict())
    #     return nodes
    
    def graphviz_id(self, i):
        'Give a unique dot identifier for this node.'
        return 'node_%s' % str(i) if i >= 0 else '_'+str(-i)
    
    def graphviz_nodes(self, i=0):
        '''
        Returns all the nodes of the tree in dot format, i.e.,
        
        node_name [label=foo]
        '''
        s = '%s [label=%s]\n' % (self.graphviz_id(i), self.value)
        if self.left:
            s += self.left.graphviz_nodes(i + 1)
        if self.right:
            s += self.right.graphviz_nodes(i - 1)
        return s
    
    def graphviz_edges(self, i=0):
        '''
        Returns all the edges of the tree in dot format, i.e.,
        
        node_name -> other_node [label=foo]
        '''
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
    '''
    Reads in a tree. Input should be a filename, the contents of which
    are formatted as
    
    value [0|1] [0|1]
    
    where a 0 indicates that a tree should be popped and made either
    the left or right child, respectively.
    '''
    stack = []
    for line in open(filename):
        vals = line.split(' ')
        t = Tree(vals[0])
        if vals[1] == '1':
            t.left = stack.pop()
        if vals[2] == '1':
            t.right = stack.pop()
        stack.append(t)
    return stack.pop()

def to_graphviz(tree):
    'Returns the dot represention of this tree. Nothing too fancy.'
    s = 'digraph {\n'
    s += tree.graphviz_nodes()
    s += tree.graphviz_edges()
    # s += '\n'.join(['\tnode%d [label=%s]' % (x, label) for x, label in zip(xrange(len(nodes)), nodes.values())])
    s += '\n}'
    return s

def main():
    print(to_graphviz(read_tree('treetest')))

if __name__ == '__main__':
    main()
