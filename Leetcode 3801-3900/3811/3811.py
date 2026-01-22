# Leetcode 3811: Number of Alternating XOR Partitions
# https://leetcode.com/problems/number-of-alternating-xor-partitions/
# Solved on 22nd of January, 2026
class Solution:
    def alternatingXOR(self, nums: list[int], target1: int, target2: int) -> int:
        """
        Calculates the number of ways to partition the array into subarrays such that
        the XOR sum of the subarrays alternates between target1 and target2.

        Args:
            nums (list[int]): The input list of integers.
            target1 (int): The target XOR sum for the 1st, 3rd, 5th, ... subarrays.
            target2 (int): The target XOR sum for the 2nd, 4th, 6th, ... subarrays.

        Returns:
            int: The total number of valid alternating XOR partitions modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        counts = {0: [0, 1]}
        currentXor = 0
        ways1 = 0
        ways2 = 0

        for num in nums:
            currentXor ^= num

            xor1 = currentXor ^ target1
            if xor1 in counts:
                ways1 = counts[xor1][1]
            else:
                ways1 = 0

            xor2 = currentXor ^ target2
            if xor2 in counts:
                ways2 = counts[xor2][0]
            else:
                ways2 = 0

            if currentXor not in counts:
                counts[currentXor] = [0, 0]

            counts[currentXor][0] = (counts[currentXor][0] + ways1) % mod
            counts[currentXor][1] = (counts[currentXor][1] + ways2) % mod

        return (ways1 + ways2) % mod