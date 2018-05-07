class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        d = [False] * (len(s)+1)
        d[0] = True
        maxL = 0
        if len(dict) > 0:
            maxL = max([len(i) for i in dict])
        for i in range(1, len(s)+1):
            for j in range(1, maxL+1):
                if i >= j and d[i-j] and s[i-j:i] in dict:
                    d[i] = True
                    break
        return d[len(s)]