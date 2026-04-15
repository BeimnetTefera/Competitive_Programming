class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.helper(n)

    def helper(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True

        if n % 4 == 0:
            return self.helper(n//4)
        else:
            return False