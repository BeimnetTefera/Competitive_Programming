class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(left, right, s):
            # if the traverse ends they are same so return true
            if left >= right:
                return True

            # check if both are alphabet and not same no need to check return false
            if s[left].isalnum() and s[right].isalnum():
                
                if s[left].lower() != s[right].lower():
                    return False

            if not s[left].isalnum():
                return helper(left + 1, right, s)

            elif not s[right].isalnum():
                return helper(left, right - 1, s)

            else:
                return helper(left + 1, right - 1, s)

        return helper(0, len(s) - 1, s)