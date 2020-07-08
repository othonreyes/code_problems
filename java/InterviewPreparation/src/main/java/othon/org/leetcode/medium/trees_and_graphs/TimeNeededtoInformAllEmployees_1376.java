package othon.org.leetcode.medium.trees_and_graphs;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayList;
import java.util.List;

/**
 * Link: https://leetcode.com/problems/time-needed-to-inform-all-employees/
 * <p>
 * TODO:
 */

@Slf4j
public class TimeNeededtoInformAllEmployees_1376 {
    public static void main(String[] args) {
        Solution s = new Solution();
        int n = 7, headID = 6;
        int[] manager = {1,2,3,4,5,6,-1};
        int[] informTime = {0,6,5,4,3,2,1};
        log.info("{}", s.numOfMinutes(n, headID, manager, informTime));
    }

    static class Solution {
        public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
            if (n==1) {
                return 0;
            }
            Node[] nodes = new Node[n];
            for (int i=0; i < n; i++) {
                nodes[i] = new Node(i, informTime[i]);
                if (i != headID) {
                    if(nodes[manager[i]] == null) {
                        nodes[manager[i]] = new Node(manager[i], informTime[manager[i]]);
                    }
                    nodes[manager[i]].adjacent.add(nodes[i]);
                }
            }

            return dfs(nodes[headID]);
        }

        int dfs(Node node) {
            if (node == null) {
                return 0;
            }
            int accumulatedTime = 0;
            for (Node child : node.adjacent) {
                accumulatedTime += dfs(child);
            }
            accumulatedTime += node.time;
            return accumulatedTime;
        }

        class Node {
            int ix;
            int time;
            List<Node> adjacent = new ArrayList<>();

            Node (int ix , int time) {
                this.ix = ix;
                this.time = time;
            }
        }
    }
}
