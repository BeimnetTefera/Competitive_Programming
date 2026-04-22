class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this function loop through the array and count how long does it take
        def canEat(mid, h):
            time_taken = 0
            for num in piles:
                time_taken += math.ceil(num / mid)
            return True if time_taken <= h else False

        # to finish koko can eat at min the smallest value from an array and at max he has to eat the larget value
        # so the range is from smallest value to larget value
        min_eat = 1
        max_eat = max(piles)
        # this loop controls the binary search algorithm
        while min_eat <= max_eat:
            mid = min_eat + (max_eat - min_eat) // 2

            if canEat(mid, h):
                max_eat = mid - 1
            else:
                min_eat = mid + 1

        return min_eat