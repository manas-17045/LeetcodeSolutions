# Leetcode 2563: Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        def binary_search_left(target, start):
            left, right = start, n - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search_right(target, start):
            left, right = start, n - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return left

        for i in range(n - 1):
            left = binary_search_left(lower - nums[i], i + 1)
            right = binary_search_right(upper - nums[i], i + 1)

            if left <= right and nums[left] + nums[i] >= lower and nums[right] + nums[i] <= upper:
                count += right - left + 1

        return count