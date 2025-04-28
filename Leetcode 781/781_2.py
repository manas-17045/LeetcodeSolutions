# Leetcode 781: Rabbits in Forest
# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        if not answers:
            return 0

        # Count the frequency of each answer
        count_map = {}
        for answer in answers:
            count_map[answer] = count_map.get(answer, 0) + 1

        total_rabbits = 0

        # Process each unique answer
        for answer, frequency in count_map.items():
            # Each color group has (answer + 1) rabbits
            group_size = answer + 1

            # Calculate complete groups and any remainder
            complete_groups = frequency // group_size
            remainder = frequency % group_size

            # If there's a remainder, we need one more complete group
            if remainder > 0:
                complete_groups += 1

            # Add to total
            total_rabbits += complete_groups * group_size

        return total_rabbits