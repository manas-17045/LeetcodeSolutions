# Leetcode 3630: Partition Array for Maximum XOR and AND
# https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/
# Solved on 26th of November, 2025
class Solution:
    def maximizeXorAndXor(self, nums: list[int]) -> int:
        """
        This function aims to partition the input array `nums` into three subarrays A, B, and C
        such that the expression `AND(B) + XOR(A) + XOR(C)` is maximized.
        :param nums: A list of integers.
        :return: The maximum possible value of `AND(B) + XOR(A) + XOR(C)`.
        """
        n = len(nums)
        maxVal = 0

        def dfs(index, currentAnd, isBEmpty, xorSumRem, basis):
            nonlocal maxVal
            if index == n:
                # Leaf: Calculate max XOR sum for A using projected basis
                # We want to maximize (XOR(A) & ~S)
                mask = ~xorSumRem
                tempBasis = []

                # Re-build a reduced basis for the projected values
                for b in basis:
                    val = b & mask
                    for tb in tempBasis:
                        val = min(val, val ^ tb)
                    if val > 0:
                        tempBasis.append(val)
                        tempBasis.sort(reverse=True)

                candidate = 0
                for b in tempBasis:
                    candidate = max(candidate, candidate ^ b)

                valB = 0 if isBEmpty else currentAnd
                # Formula: AND(B) + XOR(A) + XOR(C) = AND(B) + S + 2 * (XOR(A) & ~S)
                total = valB + xorSumRem + 2 * candidate

                if total > maxVal:
                    maxVal = total
                return

            # Branch 1: Assign nums[index] to B
            nextAnd = nums[index] if isBEmpty else (currentAnd & nums[index])
            dfs(index + 1, nextAnd, False, xorSumRem, basis)

            # Branch 2: Assign nums[index] to AC (A or C)
            # Update the linear basis with the new element
            x = nums[index]
            for b in basis:
                x = min(x, x ^ b)

            if x > 0:
                basis.append(x)
                dfs(index + 1, currentAnd, isBEmpty, xorSumRem ^ nums[index], basis)
                basis.pop()  # Backtrack
            else:
                dfs(index + 1, currentAnd, isBEmpty, xorSumRem ^ nums[index], basis)

        dfs(0, 0, True, 0, [])
        return maxVal