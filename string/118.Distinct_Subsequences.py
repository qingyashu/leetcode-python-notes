class Solution:
    res = 0
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        d = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
        for i in range(len(S)+1):
          d[i][0] = 1
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                if j > i:
                    break
                if S[i-1] == T[j-1]:
                    d[i][j] = d[i-1][j-1] + d[i-1][j]
                else:
                    d[i][j] = d[i-1][j]
        return d[len(S)][len(T)]