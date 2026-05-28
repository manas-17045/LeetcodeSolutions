// Leetcode 3093: Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/
// Solved on 28th of May, 2026
class Solution {
    class TrieNode {
        int bestIndex;
        TrieNode[] children;

        TrieNode(int index) {
            this.bestIndex = index;
            this.children = new TrieNode[26];
        }
    }

    /**
     * Finds the index of the string in wordsContainer that shares the longest common suffix with each query.
     * 
     * @param wordsContainer An array of strings to search from.
     * @param wordsQuery An array of query strings to find the longest common suffix for.
     * @return An array of indices from wordsContainer corresponding to each query.
     */
    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {
        TrieNode root = new TrieNode(0);

        for (int i = 0; i < wordsContainer.length; i++) {
            String word = wordsContainer[i];
            
            if (word.length() < wordsContainer[root.bestIndex].length() || 
               (word.length() == wordsContainer[root.bestIndex].length() && i < root.bestIndex)) {
                root.bestIndex = i;
            }
            
            TrieNode current = root;
            for (int j = word.length() - 1; j >= 0; j--) {
                int charIndex = word.charAt(j) - 'a';
                if (current.children[charIndex] == null) {
                    current.children[charIndex] = new TrieNode(i);
                }
                current = current.children[charIndex];
                
                if (word.length() < wordsContainer[current.bestIndex].length() || 
                   (word.length() == wordsContainer[current.bestIndex].length() && i < current.bestIndex)) {
                    current.bestIndex = i;
                }
            }
        }

        int[] result = new int[wordsQuery.length];
        
        for (int i = 0; i < wordsQuery.length; i++) {
            String query = wordsQuery[i];
            TrieNode current = root;
            
            for (int j = query.length() - 1; j >= 0; j--) {
                int charIndex = query.charAt(j) - 'a';
                if (current.children[charIndex] == null) {
                    break;
                }
                current = current.children[charIndex];
            }
            result[i] = current.bestIndex;
        }

        return result;
    }
}