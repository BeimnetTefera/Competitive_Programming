class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        mov = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                mov[start] += 1
                mov[end + 1] -= 1
            else:
                mov[start] -= 1
                mov[end + 1] += 1

        final_mov = [mov[0]]
        running_sum = mov[0]
        for i in range(1, len(mov)):
            running_sum += mov[i]
            final_mov.append(running_sum)

        result = []
        for j in range(len(s)):
            shift = final_mov[j]
            ans = (ord(s[j]) - ord("a") + shift) % 26 + ord("a")
            result.append(chr(ans))

        return "".join(result)