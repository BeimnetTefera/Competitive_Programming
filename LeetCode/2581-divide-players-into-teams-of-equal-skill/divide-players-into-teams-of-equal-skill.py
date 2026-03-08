class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        total = sum(skill)
        size = len(skill)

        target = total // (size // 2)

        store = Counter(skill)
        chemistry = 0

        for val in skill:
            
            need = target - val

            if store[need] > 0:
                chemistry += (val * need)
                store[need] -= 1
            else: 
                return -1

        return chemistry // 2
