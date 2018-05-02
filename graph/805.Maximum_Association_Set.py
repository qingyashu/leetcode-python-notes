class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        conn = {}
        setSize = {}
        maxSize = 0
        maxSizeSet = None
        for (a, b) in zip(ListA, ListB):
            x = self.find(conn, a)
            y = self.find(conn, b)
            if setSize.get(x) is None:
                setSize[x] = 1
            if setSize.get(y) is None:
                setSize[y] = 1
            if x != y:
                conn[x] = y
                setSize[y] += setSize[x]
                if maxSize < setSize[y]:
                    maxSize = setSize[y]
                    maxSizeSet = y
        result = [maxSizeSet]
        for i in conn.keys():
            x = self.find(conn, i)
            if x == maxSizeSet:
                result.append(i)
        return result
    
    def find(self, conn, v):
        while conn.get(v) is not None:
            v = conn[v]
        return v