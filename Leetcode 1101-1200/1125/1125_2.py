# Leetcode 1125: Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/
# Solved on 10th of August, 2025
class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        """
        Finds the smallest team of people that collectively possess all required skills.
        :param req_skills: A list of strings representing the required skills.
        :param people: A list of lists of strings, where each inner list represents the skills of a person.
        :return: A list of integers representing the indices of the people in the smallest sufficient team.
        """
        # Map each skill to a bit position
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)
        full_mask = (1 << m) - 1

        # Convert each person to a bitmask of skills
        people_masks = []
        for p in people:
            mask = 0
            for s in p:
                if s in skill_index:
                    mask |= 1 << skill_index[s]
            people_masks.append(mask)

        dp = {0: []}

        for i, pMask in enumerate(people_masks):
            if pMask == 0:
                # this person adds no new required skill, skip
                continue

            # Iterate over a snapshot of current dp items to avoid modifying during iteration
            for cur_mask, team in list(dp.items()):
                new_mask = cur_mask | pMask
                # If new_mask not seen or we found a smaller team, update
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]

        return dp[full_mask]