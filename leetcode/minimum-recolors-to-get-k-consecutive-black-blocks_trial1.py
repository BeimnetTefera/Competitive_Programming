class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        store = Counter(blocks[:k])
        min_cnt = store["W"]
        cnt = store["W"]
        left = 0

        for right in range(k, len(blocks)):

            store[blocks[left]] -= 1
            if blocks[left] == "W":
                cnt -= 1
            left += 1

            store[blocks[right]] += 1
            if blocks[right] == "W":
                cnt += 1
            
            min_cnt = min(cnt, min_cnt)

        return min_cnt