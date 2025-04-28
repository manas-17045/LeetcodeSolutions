# Leetcode 38: Count and Say
# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        # Start with the first term of the sequence
        current_string = "1"

        # Iterate from the 2nd term to the nth term
        for _ in range(2, n + 1):
            next_string = ""
            i = 0 # Pointer to iterate through the current_string

            while i < len(current_string):
                char = current_string[i] # Get the current character
                count = 0 # Initialize count for the current character

                # Count the consecutive occurrences of the current character
                j = i
                while j < len(current_string) and current_string[j] == char:
                    count += 1
                    j += 1

                # Append the count and the character to the next_string
                next_string += str(count) + char

                # Move the pointer to the next distinct character
                i = j

            # Update the current_string for the next iteration to the newly generated string
            current_string = next_string

        return current_string