class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [0] * len(s)

        for char, idx in zip(s, indices):
            shuffled[idx] = char

        return ''.join(shuffled)