class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [char for char in s if char.isalnum()]
        

        left = 0
        right = len(word) - 1

        while left < right:
            if word[right].lower() != word[left].lower():
                return False
            else:
                left += 1
                right -= 1

        return True