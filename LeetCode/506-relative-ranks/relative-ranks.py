class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        ranked = sorted(score, reverse = True)
        store = {}

        for i in range(len(score)):
            store[ranked[i]] = store.get(ranked[i], i)
        print(store)

        result = []

        for i in range(len(score)):
            if store[score[i]] == 0:
                result.append("Gold Medal")
            elif store[score[i]] == 1:
                result.append("Silver Medal")
            elif store[score[i]] == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(store[score[i]] + 1))

        return result