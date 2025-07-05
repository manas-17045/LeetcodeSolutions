# Leetcode 2122: Recover the Original Array
# https://leetcode.com/problems/recover-the-original-array/
# Solved on 5th of July, 2025
import collections


class Solution:
    def recoverArray(self, nums: list[int]) -> list[int]:
        """
        Recovers the original array from a given array `nums` which is formed by
        taking an original array `arr`, creating `arr_lower` by subtracting `k` from
        each element of `arr`, creating `arr_upper` by adding `k` to each element of `arr`,
        and then concatenating and shuffling `arr_lower` and `arr_upper`.

        Args:
            nums: A list of integers representing the shuffled `arr_lower` and `arr_upper`.

        Returns:
            A list of integers representing the recovered original array `arr`.
        """
        size = len(nums)
        n = size // 2

        nums.sort()

        for j in range(1, size):
            difference = nums[j] - nums[0]

            if difference > 0 and difference % 2 == 0:
                k = difference // 2

                counts = collections.Counter(nums)
                originalArr = []
                isPossible = True

                for num in nums:
                    if counts[num] == 0:
                        continue

                    counts[num] -= 1
                    partner = num + 2 * k

                    if counts.get(partner, 0) > 0:
                        counts[partner] -= 1
                        originalArr.append(num + k)
                    else:
                        isPossible = False
                        break

                if isPossible:
                    return originalArr

        return []