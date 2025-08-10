# Leetcode 1125: Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/
# Solved on 10th of August, 2025
class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        """
        Finds the smallest sufficient team to cover all required skills.

        Args:
            req_skills: A list of strings representing the required skills.
            people: A list of lists of strings, where each inner list represents the skills of a person.
        Returns:
            A list of integers representing the indices of the people in the smallest sufficient team.
        """
        numSkills = len(req_skills)
        skillMap = {skill: i for i, skill in enumerate(req_skills)}

        # dp[mask] stores the smallest team for the skill combination represented by 'mask'.
        dp = {0: []}

        for personIndex, personSkills in enumerate(people):
            personSkillMask = 0
            for skill in personSkills:
                personSkillMask |= (1 << skillMap[skill])

            if personSkillMask == 0:
                continue

            currentMasks = list(dp.keys())
            for prevMask in currentMasks:
                newMask = prevMask | personSkillMask

                if newMask == prevMask:
                    continue

                prevTeam = dp[prevMask]
                newTeam = prevTeam + [personIndex]

                if newMask not in dp or len(newTeam) < len(dp[newMask]):
                    dp[newMask] = newTeam

        targetMask = (1 << numSkills) - 1
        return dp[targetMask]