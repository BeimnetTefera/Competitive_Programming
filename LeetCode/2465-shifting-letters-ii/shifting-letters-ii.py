class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        

        """
        0 = bwd
        1 = fwd

            0 - 1 ==> bwd
        abc --> zac

            1 - 2 ==> fwd
        zac --> zbd

            0 - 2 ==> fwd
        zbd -- ace
        """
        chars = [l for l in s]
        store = [0] * (len(s) + 1)

        for start, end, step in shifts:
            if step == 0:
                store[start] -= 1
                store[end + 1] += 1
            else:
                store[start] += 1
                store[end + 1] -= 1 

        result = []
        running_sum = 0
        for j in range(len(store)):
            running_sum += store[j]
            result.append(running_sum)

        ans = []
        for i in range(len(chars)):
            shift = result[i] % 26  
            new_char = (ord(chars[i]) - ord('a') + shift) % 26 + ord('a')
            ans.append(chr(new_char))   

        return "".join(ans)