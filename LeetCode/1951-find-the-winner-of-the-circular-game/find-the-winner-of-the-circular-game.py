class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        deq = deque(range(1, n+1))
        count = 0

        def helper(deq, count):

            if len(deq) == 1:
                return deq[0]

            val = deq.popleft()
            count += 1

            if k == count:
                return helper(deq, 0)
            else:
                deq.append(val)
                return helper(deq, count)
        
        return helper(deq, count)