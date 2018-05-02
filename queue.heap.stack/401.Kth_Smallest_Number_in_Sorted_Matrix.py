from heapq import heappush, heappop
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        hp = []
        r = len(matrix)
        c = len(matrix[0])
        for i in range(c):
            heappush(hp, (matrix[0][i], [0, i]))
        cnt = 0
        while cnt < k-1:
            val, pos = heappop(hp)
            cnt += 1
            if pos[0] == r-1:
                continue
            heappush(hp, (matrix[pos[0]+1][pos[1]], [pos[0]+1, pos[1]]))
        return heappop(hp)[0]