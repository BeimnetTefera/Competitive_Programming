class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        score = 0

        size = len(piles)

        step = size / 3
        turn = size - 2

        while step > 0:

            score += piles[turn]
            step -= 1
            turn -= 2
            
        return score