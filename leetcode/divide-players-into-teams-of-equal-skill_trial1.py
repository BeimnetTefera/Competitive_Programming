class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        left = 1
        right = len(skill) - 2

        skill_needed = skill[0] + skill[-1]
        chemistry = skill[0] * skill[-1]

        while left < right:
            cur_skill = skill[left] + skill[right]

            if cur_skill != skill_needed:
                return -1

            else:
                chemistry += (skill[left] * skill[right])

            left += 1
            right -= 1

        return chemistry