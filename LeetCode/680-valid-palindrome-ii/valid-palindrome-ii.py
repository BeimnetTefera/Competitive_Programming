class Solution:
    def validPalindrome(self, s: str) -> bool:
        #  left and right start at the back
        # the pointers move until they cross eachother
        # count when characters don't match until it exceds one

        left, right = 0, len(s) - 1
        while left < right:

            if s[left] != s[right]:
                l1, r1 = left + 1, right
                l2, r2 = left , right - 1

                while l1 < r1 and s[l1] == s[r1]:
                    l1 += 1
                    r1 -= 1

                while l2 < r2 and s[l2] == s[r2]:
                    l2 += 1
                    r2 -= 1

                return l1 >= r1 or l2 >= r2

            left += 1
            right -= 1

        return True