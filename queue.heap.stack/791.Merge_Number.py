from heapq import heappush, heappop
class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        if not numbers:
            return 0
        hp = []
        for num in numbers:
            heappush(hp, num)
        res = 0
        while len(hp) > 1:
            p = heappop(hp)
            q = heappop(hp)
            res += p + q
            heappush(hp, p+q)
        return res