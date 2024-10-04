class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2 != 0:
            return -1

        skill.sort()
        l = 0
        r = len(skill) - 1

        total = 0
        teamSkill = skill[0] + skill[-1]

        while l < r:
            if skill[l] + skill[r] != teamSkill:
                return -1

            total += skill[l] * skill[r]
            l += 1
            r -= 1
        
        return total
        

