class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        chars.sort(key=self.cmp)
        
    def cmp(self, c):
        if c >= 'a' and c <= 'z':
            return ord(c) - ord('a')
        else:
            return ord(c) - ord('A') + 26
        