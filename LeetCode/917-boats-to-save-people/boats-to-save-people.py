class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people) - 1
        right = size
        left, boats = 0, 0
        
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1

            right -= 1
            
            boats += 1

        return boats