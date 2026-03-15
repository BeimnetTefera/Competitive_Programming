class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = Counter(s1)
        left = 0
        right = len(s1)
        cur_sub = Counter(s2[:right])

        if needed == cur_sub:
            return True

        for i in range(right, len(s2)):

            cur_sub[s2[left]] -= 1
            if cur_sub[s2[left]] == 0:
                del cur_sub[s2[left]]
            left += 1

            cur_sub[s2[i]] = cur_sub.get(s2[i], 0) + 1

            if needed == cur_sub:
                return True

        return False