class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        step = 0
        for seat, std in zip(seats, students):
            step += abs(seat - std)

        return step