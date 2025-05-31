# Leetcode 3171: Find Subarray With Bitwise OR Closest to K
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/
# Solved on 31st of May, 2025

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        # Initialize 'minABSDiff' to positive infinity.
        # This ensures that any valid difference calculated will be smaller and become the new minimum.
        minABSDiff = float('inf')

        # 'possibleORSEndingAtPrev' is a set that will store the distinct bitwise OR values
        # of all contiguous subarrays that end at the element *just before* the current one in the loop.
        # It's initialized as empty because, before processing the first element, there are no prior subarrays.
        possibleORSEndingAtPrev = set()

        # Iterate through each number 'num' in the input list 'nums'.
        # 'num' represents the current element nums[j] being processed.
        for num in nums:
            # 'possibleORSEndingAtCurr' will store distinct bitwise ORs of subarrays ending at the current 'num'.
            # It's reinitialized for each 'num'.
            possibleORSEndingAtCurr = set()

            # Case 1: Consider the subarray that consists of only the current element 'num'.
            # The bitwise OR of such a subarray (e.g., nums[j...j] is simply 'num' itself.
            possibleORSEndingAtCurr.add(num)

            # Case 2: Consider subarrays formed by extending those subarrays that ended at the previous element.
            # Iterate through each 'prevORVal' from 'possibleORSEndingAtPrev'.
            # 'prevORVal' is the OR sum of a subarray like nums[i...j-1].
            for prevORVal in possibleORSEndingAtPrev:
                # The OR sum of the extended subarray nums[i...j] is 'prevORVal | num'.
                newORVal = prevORVal | num
                # Add this new OR value to the set for subarrays ending at the current 'num'.
                # Using a set automatically handles duplicates, ensuring distinct values.
                possibleORSEndingAtCurr.add(newORVal)

            # After computing all possible OR values for subarrays ending at the current 'num',
            # iterate through these OR values.
            for currentORVal in possibleORSEndingAtCurr:
                # For each 'currentORVal', calculate its absolute difference with the target 'k'.
                diff = abs(currentORVal - k)
                # If this 'diff' is smaller than any found so far, update 'minABSDiff'.
                minABSDiff = min(minABSDiff, diff)

            # Prepare for the next iteration.
            # The set of ORs calculated for the current element ('possibleORSEndingAtCurr')
            # will become the set of ORs for subarrays ending at the "previous" element
            # relative to the next element in 'nums'.
            possibleORSEndingAtPrev = possibleORSEndingAtCurr

        # After iterating through all numbers in 'nums' and considering all relevant subarrays,
        # 'minABSDiff' will hold the minimum possible absolute difference.
        return minABSDiff