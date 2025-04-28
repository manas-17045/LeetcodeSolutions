# Leetcode 781: Rabbits in Forest
# https://leetcode.com/problems/rabbits-in-forest/

import collections


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        if not answers:
            return 0

        counts = collections.Counter(answers)
        total_rabbits = 0

        for x, count in counts.items():
            '''
            x = the answer given ("number of "other" rabbits with the same color")
            count = how many rabbits gave this answer 'x'
            Rabbits answering 'x' bekong to groups of size 'x + 1'. 
            '''
            group_size = x + 1

            '''
            Calculate the minimum number of groups of this size needed.
            Each group can account for 'group_size' rabbits all answering 'x'.
            Use ceiling division: ceil(count / group_size)
            '''

            # Integer arithmetic version for ceiling: (numerator + denominator - 1) // denominator
            num_groups = (count + group_size - 1) // group_size

            # Alternative using math.ceil (requires float division):
            # num_groups = math.ceil(count / group_size)

            # Add the total number of rabbits belonging to these necessary groups.
            # Each of the 'num_groups' contributes 'group_size' rabbits to the total.
            total_rabbits += num_groups * group_size

        return total_rabbits