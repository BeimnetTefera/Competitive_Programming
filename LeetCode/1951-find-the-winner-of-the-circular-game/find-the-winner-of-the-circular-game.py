class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        deq = deque()
        for i in range(1, n + 1):
            deq.append(i)

        count = 0

        while len(deq) > 1:
            val = deq.popleft()
            count += 1

            if k == count:
                count = 0
                continue

            deq.append(val)
        return deq[0]