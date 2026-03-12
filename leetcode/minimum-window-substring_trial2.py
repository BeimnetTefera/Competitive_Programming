class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        m = len(s)
        n = len(t)
        ans = ""

        if n > m:
            return ans

        needed = Counter(t)

        left, len_ans = 0 , float("inf")

        cur_substring = Counter(s[:n])

        case = True
        for char, freq in needed.items():
            cur_freq = cur_substring[char]

            if cur_freq < freq:
                case = False
                break

        if case:
            while True:

                valid = True
                for char, freq in needed.items():
                    if cur_substring[char] < freq:
                        valid = False
                        break

                if not valid:
                    break

                if n - left < len_ans:
                    len_ans = n - left 
                    ans = s[left:n]

                cur_substring[s[left]] -= 1
                left += 1
        
        for right in range(n, m):

            cur_substring[s[right]] = cur_substring.get(s[right], 0) + 1

            case = True
            for char, freq in needed.items():
                cur_freq = cur_substring[char]

                if cur_freq < freq:
                    case = False
                    break


            if case:
                while True:

                    valid = True
                    for char, freq in needed.items():
                        if cur_substring[char] < freq:
                            valid = False
                            break

                    if not valid:
                        break

                    if right - left + 1 < len_ans:
                        len_ans = right - left + 1
                        ans = s[left:right+1]

                    cur_substring[s[left]] -= 1
                    left += 1

        return ans