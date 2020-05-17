package othon.org.leetcode.hard.recursion;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Link: https://leetcode.com/problems/word-search-ii
 *
 * TODO:
 *  try with a trie
 */
@Slf4j
public class WrodSearchII {
    public static void main(String[] args) {
        Solution s = new Solution();
        var input = "";
    }


    static class TrieSolution {
        char[][] board;
        List<String> result = new ArrayList<>();

        static class TrieNode {
            Map<Character, TrieNode> children = new HashMap<>();
            String word;
        }
        public List<String> findWords(char[][] b, String[] words) {
            // Convert the words to a trie
            TrieNode root = new TrieNode();
            for (String w: words) {
                TrieNode n = root;
                for (int i = 0; i < w.length(); i++) {
                    Character c = w.charAt(i);
                    if (!n.children.containsKey(c)) {
                        n.children.put(c, new TrieNode());
                    }
                    n = n.children.get(c);
                }
                n.word = w;
            }
            this.board = b;
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    backtrack(i,j, root);
                }
            }
            return result;
        }

        static int[][] directions = {{-1,0}, {1,0}, {0,1}, {0,-1}};

        private void backtrack(int i, int j, TrieNode root) {
            Character letter = board[i][j];
            TrieNode n = root.children.get(letter);

            // not a valid word
            if (n == null) {
                return;
            }

            // if we found a word then resolve
            if (n != null && n.word != null) {
                result.add(n.word);
                n.word = null; // erase the word so we don't need to look it up again
                //return; // commented because we want to continue searching
            }
            // otherwise it's time to explore
            board[i][j] = '#'; // temporarily erase the word
            //explore in 4 directions
            for (int k = 0; k < directions.length; k++) {
                int[] d = directions[k];
                int newI = i + d[0];
                int newJ = j + d[1];
                if (newI<0 || newJ < 0 || i>=board.length || j >= board[0].length)
                    continue;
                if (n.children.containsKey(board[newI][newJ]))
                    backtrack(newI, newJ, n);
            }
            //restore the word so backtracking
            board[i][j] = letter;
        }

    }

    static class Solution {
        static int[][] directions = {{-1,0}, {1,0}, {0,1}, {0,-1}};
        public List<String> findWords(char[][] board, String[] words) {
            // iterate over the words
            // for each word have a set of visited nodes key = char-y-x
            // if not visited then explore that one
            List<String> results = new ArrayList<>();
            for (String word : words) {
                char[] wordArr = word.toCharArray();

                int r = board.length;
                int c = board[0].length;
                boolean found = false;
                for (int i=0;i<r && !found;i++) {
                    for (int j=0; j < c && !found; j++) {
                        if (board[i][j] == wordArr[0]) {
                            Set<String> visited = new HashSet<>();
                            if (found(wordArr,0,visited, board, i,j,r,c)) {
                                results.add(word);
                                found = true;
                            }
                        }
                    }
                }
            }
            return results;
        }

        boolean found(char[] wordArr, int ix, Set<String> visited, char[][] board, int i, int j, int r, int c) {
            visited.add(Character.toString(wordArr[ix]) + "-" + String.valueOf(i) + "-" + String.valueOf(j));
            ix += 1;
            if (ix==wordArr.length) {
                return true;
            }
            boolean found = false;
            for (int k= 0; k < directions.length; k++) {
                int newI = i + directions[k][0];
                int newJ = j + directions[k][1];
                String newKey = Character.toString(wordArr[ix]) + "-" + String.valueOf(newI) + "-" + String.valueOf(newJ);
                if (newI< 0 || newJ < 0 || newI == r || newJ == c || wordArr[ix] != board[newI][newJ]
                        || visited.contains(newKey)) {
                    continue;
                }
                found |= found(wordArr,ix,visited, board, newI, newJ,r,c);
            }
            return found;
        }
    }
}
