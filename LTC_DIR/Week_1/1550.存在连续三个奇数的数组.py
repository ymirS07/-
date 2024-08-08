class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        return n >= 3 and any(arr[i] & 1 and arr[i+1] & 1 and arr[i+2] & 1 for i in range (n - 2))
