class Solution:
    def isPalindrome(self, s: str) -> bool:

        def helper(left, right):
            #   base case
            if left >= right:
                return True

            # if both of them are alnum check 
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
            # both of them are not alnum move the ptr
            if not s[left].isalnum() and not s[right].isalnum():
                return helper(left + 1, right - 1)
            # if left one is not move it
            elif not s[left].isalnum():
                return helper(left + 1, right)
            # if right is not move it
            elif not s[right].isalnum():
                return helper(left, right - 1)

            return helper(left + 1, right - 1)

        return helper(0, len(s)-1)