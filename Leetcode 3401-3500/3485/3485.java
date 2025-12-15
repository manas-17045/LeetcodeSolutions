// Leetcode 3485: Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/
// Solved on 15th of December, 2025
class Solution {
    class Node {
        Node[] next = new Node[26];
        int count = 0;
        int depth;
        int maxDepth = -1;

        Node(int depth) {
            this.depth = depth;
        }
    }

    /**
     * Calculates the longest common prefix for each word in the input array `words`
     * after removing `k` strings.
     * @param words An array of strings.
     * @param k The number of strings to remove.
     * @return An array of integers, where `answer[i]` is the length of the longest common prefix
     *         for `words[i]` after removing `k` strings.
     */
    public int[] longestCommonPrefix(String[] words, int k) {
        Node root = new Node(0);
        for (String word : words) {
            Node curr = root;
            curr.count++;
            for (char c : word.toCharArray()) {
                int index = c - 'a';
                if (curr.next[index] == null) {
                    curr.next[index] = new Node(curr.depth + 1);
                }
                curr = curr.next[index];
                curr.count++;
            }
        }

        calculateMaxDepth(root, k);

        int n = words.length;
        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            if (root.count <= k) {
                answer[i] = 0;
                continue;
            }

            Node curr = root;
            int maxOffPath = 0;
            int maxOnPath = 0;

            String word = words[i];
            for (char c : word.toCharArray()) {
                int index = c - 'a';
                for (int j = 0; j < 26; j++) {
                    if (j != index && curr.next[j] != null) {
                        maxOffPath = Math.max(maxOffPath, curr.next[j].maxDepth);
                    }
                }
                curr = curr.next[index];
                if (curr.count > k) {
                    maxOnPath = curr.depth;
                }
            }

            for (int j = 0; j < 26; j++) {
                if (curr.next[j] != null) {
                    maxOffPath = Math.max(maxOffPath, curr.next[j].maxDepth);
                }
            }

            answer[i] = Math.max(maxOffPath, maxOnPath);
        }

        return answer;
    }

    private void calculateMaxDepth(Node node, int k) {
        node.maxDepth = (node.count >= k) ? node.depth : -1;
        for (Node child : node.next) {
            if (child != null) {
                calculateMaxDepth(child, k);
                node.maxDepth = Math.max(node.maxDepth, child.maxDepth);
            }
        }
    }
}