class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.conn = [-1] * n
        self.cnt = n

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        x = self.find(a-1)
        y = self.find(b-1)
        if x != y:
            self.conn[x] = y
            self.cnt -= 1
    
    def find(self, k):
        while self.conn[k] != -1:
            k = self.conn[k]
        return k

    """
    @return: An integer
    """
    def query(self):
        return self.cnt