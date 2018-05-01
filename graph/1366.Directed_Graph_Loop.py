class GraphNode:
    def __init__(self, x):
        self.val = x
        self.out = [] # labels 

class Graph:
    def __init__(self):
        self.V = {} # label -> node
        self.recurVisited = []
        self.outerVisited = []
        self.maxLabel = 0
        
    def appendEdge(self, s, e):
        if self.V.get(s) == None:
            self.V[s] = GraphNode(s)
        if self.V.get(e) == None:
            self.V[e] = GraphNode(e)
        self.V[s].out.append(self.V[e])
        self.maxLabel = max(self.maxLabel, s, e)
        
    def hasLoopRecur(self, node):
        if self.recurVisited[node.val]:
            return True
        self.outerVisited[node.val] = True
        self.recurVisited[node.val] = True
        for nei in node.out:
            if self.hasLoopRecur(nei):
                return True
        self.recurVisited[node.val] = False
        return False

    def hasLoop(self):
        self.outerVisited = [False] * (self.maxLabel+1)
        self.recurVisited = [False] * (self.maxLabel+1)
        for v in self.V.keys():
            node = self.V[v]
            if self.outerVisited[node.val]:
                continue
            if self.hasLoopRecur(node):
                return True
        return False

class Solution:
    
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    def isCyclicGraph(self, start, end):
        g = Graph()
        for i in range(len(start)):
            s = start[i]
            e = end[i]
            g.appendEdge(s, e)
        return g.hasLoop()