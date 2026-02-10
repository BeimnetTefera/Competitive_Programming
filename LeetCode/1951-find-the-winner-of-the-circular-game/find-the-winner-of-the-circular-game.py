class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = range(1, n + 1)
        que = deque(arr)
        count = 0

        while len(que) > 1:
            num = que.popleft()
            count += 1

            if count == k:
                count = 0
                continue  
            else:
                que.append(num)

        return que[0]

