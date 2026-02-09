class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    common[list1[i]] = i + j

        result = []
        min_idx = min(common.values())
        for word, idx in common.items():
            if idx == min_idx:
                result.append(word)

        return result