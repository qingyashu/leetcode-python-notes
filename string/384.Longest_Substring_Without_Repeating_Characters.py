class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        chIndex = {}
        longest = 0
        leftLength = 0
        for i in range(len(s)):
            ch = s[i]
            if chIndex.get(ch) is None:
                chIndex[ch] = -1
            start = max(i - leftLength, chIndex[ch]+1)
            length = i - start + 1
            longest = max(longest, length)
            chIndex[ch] = i
            leftLength = length
        return longest