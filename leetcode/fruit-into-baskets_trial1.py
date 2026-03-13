class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_count  = 0, 0
        store = {}

        for right in range(len(fruits)):
            store[fruits[right]] = store.get(fruits[right], 0) + 1

            while len(store) > 2:

                store[fruits[left]] -= 1

                if store[fruits[left]] == 0:
                    del store[fruits[left]]
                
                left += 1 

            max_count = max(max_count, right - left + 1)

        return max_count