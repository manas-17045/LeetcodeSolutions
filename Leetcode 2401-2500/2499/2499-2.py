# Leetcode 2499: Minimum Total Cost to Make Arrays Unequal
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/
# Solved on 7th of October, 2025
from collections import Counter


class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum total cost to make nums1[i] != nums2[i] for all i.

        Args:
            nums1: A list of integers.
            nums2: A list of integers.
        Returns:
            The minimum total cost, or -1 if it's impossible.
        """
        n = len(nums1)

        # Find all indices where nums1[i] == nums2[i]
        swap_indices = []
        swap_values = []

        for i in range(n):
            if nums1[i] == nums2[i]:
                swap_indices.append(i)
                swap_values.append(nums1[i])

        # Base cost
        total_cost = sum(swap_indices)

        # If no swaps needed
        if not swap_indices:
            return 0

        # Count frequency of values in swap positions
        value_count = Counter(swap_values)

        # Find the most frequent value
        max_freq = max(value_count.values())
        swap_count = len(swap_indices)

        # If no value dominates (appears > half), we're done
        if max_freq * 2 <= swap_count:
            return total_cost

        # Find the dominant value
        dominant_value = None
        for val, freq in value_count.items():
            if freq == max_freq:
                dominant_value = val
                break

        # We need to add more swaps to dilute the dominant value
        needed = 2 * max_freq - swap_count

        # Find additional indices to swap
        already_swapping = set(swap_indices)
        added = 0

        for i in range(n):
            if added >= needed:
                break

            if i not in already_swapping:
                # Check if this index is safe to add
                if nums1[i] != nums2[i] and \
                        nums1[i] != dominant_value and \
                        nums2[i] != dominant_value:
                    total_cost += i
                    added += 1

        # If we couldn't find enough safe indices, it's impossible
        if added < needed:
            return -1

        return total_cost