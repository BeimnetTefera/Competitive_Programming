class Solution(object):
    def reverseString(self, s):
        return self.helper(s, 0, len(s) - 1)

    def helper(self, s, left, right):
        if left >= right:
            return 

        s[left], s[right] = s[right], s[left]
        return self.helper(s, left + 1, right - 1)