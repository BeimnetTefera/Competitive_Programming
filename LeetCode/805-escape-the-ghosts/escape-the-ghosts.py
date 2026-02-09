class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        escape_step = abs(target[0]) + abs(target[1])

        for arr in ghosts:
            ghost_step = abs(arr[0] - target[0]) + abs(arr[1] - target[1])

            if ghost_step <= escape_step:
                return False

        return True