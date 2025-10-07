# Leetcode 1488: Avoid Flood in The City
# https://leetcode.com/problems/avoid-flood-in-the-city/
# Solved on 7th of october, 2025
class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        """
        Given a list of rain events, determine a schedule to dry lakes to avoid flooding.

        Args:
            rains (list[int]): A list where rains[i] is the lake that rains on day i. 0 means no rain.
        Returns:
            list[int]: A list representing the drying schedule. ans[i] is the lake dried on day i, or 1 if no lake is dried. Returns [] if flooding is unavoidable.
        """
        n = len(rains)
        ans = [1] * n
        full_lakes = {}
        dry_days = []

        for i in range(n):
            if rains[i] == 0:
                dry_days.append(i)
            else:
                lake = rains[i]

                # Check if this lake is already full
                if lake in full_lakes:
                    # Need to dry it before today
                    filled_day = full_lakes[lake]

                    # Find a dry day between filled_day and i
                    found = False
                    for j in range(len(dry_days)):
                        if dry_days[j] > filled_day:
                            # Use this dry day
                            ans[dry_days[j]] = lake
                            dry_days.pop()
                            found = True
                            break

                    if not found:
                        return []

                # Lake becomes full
                full_lakes[lake] = i

        # Fill remaining dry days with i
        for day in dry_days:
            ans[day] = 1

        return ans