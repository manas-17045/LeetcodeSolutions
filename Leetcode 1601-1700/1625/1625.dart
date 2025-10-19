// Leetcode 1625: Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
// Solved on 19th of October, 2025
import 'dart:collection';

class Solution {

	/// Finds the lexicographically smallest string that can be obtained by applying
	/// two operations repeatedly: an "add" operation and a "rotate" operation.
	///
	/// This function performs a Breadth-First Search (BFS) to explore all
	/// possible strings reachable from the initial string [s]. It keeps track of
	/// visited strings to avoid redundant computations and cycles.
	///
	/// The operations are:
	/// 1. **Add**: For every digit at an odd index, add [a] to it (modulo 10).
	/// 2. **Rotate**: Cyclically shift the string to the left by [b] positions.
	///
	/// - [s]: The initial string of even length, consisting of digits.
	/// - [a]: The integer to add to digits at odd indices.
	/// - [b]: The number of positions to rotate the string by.
	///
	/// Returns the lexicographically smallest string found after any number of operations.
	String findLexSmallestString(String s, int a, int b) {
		String smallest = s;
		Queue<String> queue = Queue();
		Set<String> visited = {};

		queue.add(s);
		visited.add(s);

		while (queue.isNotEmpty) {
			String current = queue.removeFirst();

			if (current.compareTo(smallest) < 0) {
				smallest = current;
			}

			List<String> chars = current.split('');
			for (int i = 1; i < chars.length; i += 2) {
				int digit = int.parse(chars[i]);
				chars[i] = ((digit + a) % 10).toString();
			}
			String addS = chars.join('');

			if (visited.add(addS)) {
				queue.add(addS);
			}

			String rotateS = current.substring(current.length - b) + current.substring(0, current.length - b);
			if (visited.add(rotateS)) {
				queue.add(rotateS);
			}
		}

		return smallest;
	}
}