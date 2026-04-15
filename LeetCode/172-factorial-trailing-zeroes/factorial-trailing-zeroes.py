class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fives = 5
        zeros = 0

        while n // fives >= 1:
            zeros += (n // fives)
            fives *= 5

        return zeros