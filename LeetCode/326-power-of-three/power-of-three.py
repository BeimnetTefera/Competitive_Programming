class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return self.helper(n)

    def helper(self, n):
        if n <= 0:
            return False
        # I wanted it as base condition like after division if it reaches 
        if n == 1:
            return True
        
        if n % 3 == 0:
            n = n // 3
            return self.helper(n)
        else:
            return False


        # check if num is divisible by three if not we don't need it
        # move 2 times and the third one is to check if that number power equals the original num
        # where ever it is terminated we check it to the power of 3 and check quality to original problem
