from heapq import heappush, heappop

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        count = {}
        for word in words: 
            cnt = count.get(word, 0) + 1
            count[word] = cnt
        hp = []
        for key in count:
            heappush(hp, (-count[key], key))
        return [heappop(hp)[1] for _ in range(k)]