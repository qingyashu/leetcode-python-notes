class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        count = {}
        queue = []
        for i in nums:
            if number == i:
                for j in queue:
                    if count[j] == 1:
                        return j
                return -1
            if count.get(i) is None:
                count[i] = 0
            count[i] += 1
            if count[i] == 1:
                queue.append(i)
        return -1