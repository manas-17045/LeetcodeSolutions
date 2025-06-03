# Leetcode 1298: Maximum Candies You Can Get from Boxes
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
# Solved on 3rd of June, 2025

class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        """
        Calculates the maximum number of candies you can collect from a given set of boxes.
        """
        # Set of boxes we currently hold (but may not be able to open yet)
        availB = set(initialBoxes)

        # Set of boxes we've already opened
        visited = set()

        # Set of keys we have
        haveK = set()

        # Total candies collected
        totalCandies = 0

        # We use a flag to know if we made progress in the last pass
        madeProgress = True

        while madeProgress:
            madeProgress = False

            # Collect a list of boxes to attempt this round (so we don't modify the set while iterating)
            toCheck = list(availB)
            for box in toCheck:
                if box in visited:
                    continue

                # Check if this bix is openable (either status == 1 or we have its key)
                if status[box] == 1 or box in haveK:
                    # We can open this box now
                    visited.add(box)
                    madeProgress = True

                    # Collect candies
                    totalCandies += candies[box]

                    # Add any new keys we find inside
                    for k in keys[box]:
                        if k not in haveK:
                            haveK.add(k)

                    # Add any new boxes we find inside to our pool
                    for b in containedBoxes[box]:
                        if b not in availB and b not in visited:
                            availB.add(b)

                    # Once opened, it remains open, but we don't need to revisited it
                    # (removing from availableBoxes isn't strictly necessary, since we check visited)
                    # Moreover, to keep availableBoxes small, we should remove it.
                    availB.discard(box)

        # If we looped through all availableBoxes and didn't open any new box, we stop.
        return totalCandies