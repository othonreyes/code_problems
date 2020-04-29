package othon.org.leetcode.hard.recursion;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Link: https://leetcode.com/problems/word-search-ii
 *
 * TODO:
 *  try with a trie
 */
@Slf4j
public class WrodSearchII {
    public static void miain(String[] args) {
        Solution s = new Solution();
        var input = "";
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
