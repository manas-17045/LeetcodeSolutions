# Leetcode 3478: Choose K Elements With Maximum Sum
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/
# Solved on 29th of September, 2025
import heapq


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        """
        Calculates the maximum sum of k elements from nums2 for each element in nums1,
        considering only elements from nums2 whose corresponding nums1 value is less than or equal to the current nums1 value.

        Args:
            nums1 (list[int]): The first list of integers.
            nums2 (list[int]): The second list of integers.
            k (int): The number of largest elements to consider from nums2.

        Returns:
            list[int]: A list where each element ans[i] is the maximum sum of k elements from nums2
                       such that for each chosen nums2[j], nums1[j] <= nums1[i].
        """
        n = len(nums1)
        ans = [0] * n

        # Sort indices by nums1 value (ascending)
        idxs = list(range(n))
        idxs.sort(key=lambda i: nums1[i])

        heap = []
        current_sum = 0

        # Iterate trough sorted indices grouped by equal nums1 value
        i = 0
        while i < n:
            v = nums1[idxs[i]]
            # Collect indices belonging to this group (same nums1 value)
            j = i
            group = []
            while j < n and nums1[idxs[j]] == v:
                group.append(idxs[j])
                j += 1

            # For each index in this group, answer is the sum of up to k largest nums2 among previous groups
            for orig_idx in group:
                ans[orig_idx] = current_sum

            # After answering, add this group's nums2 values to the heap
            for orig_idx in group:
                val = nums2[orig_idx]
                if len(heap) < k:
                    heapq.heappush(heap, val)
                    current_sum += val
                else:
                    # If val is larger than smallest in heap, replace and update sum.
                    if k > 0 and heap and val > heap[0]:
                        smallest = heapq.heapreplace(heap, val)
                        current_sum += val - smallest

            i = j

        return ans