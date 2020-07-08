package othon.org.gfg.divideandconquer;

import java.util.List;
/*

Input : 4 2
        1 2 60
        3 4 50
Output :2
        1 2 60
        3 4 50
Explanation:
Connected components are:
1->2 and 3->4
Therefore, our answer is 2 followed by
1 2 60 and 3 4 50.

Input :9 6
       7 4 98
       5 9 72
       4 6 10
       2 8 22
       9 7 17
       3 1 66
Output :3
        2 8 22
        3 1 66
        5 6 10
Explanation:
Connected components are 3->1,
5->9->7->4->6 and 2->8.
Therefore, our answer is 3 followed by
2 8 22, 3 1 66, 5 6 10

 */
// https://www.geeksforgeeks.org/water-connection-problem/
public class WaterConnectionProblem {

    public static void main(String[] args) {
        int n = 9;
        int p = 6;


        int arr[][] = { { 7, 4, 98 },
                { 5, 9, 72 },
                { 4, 6, 10 },
                { 2, 8, 22 },
                { 9, 7, 17 },
                { 3, 1, 66 } };
        List<List<Integer>> results = solve(n, p, arr);
    }

    private static List<List<Integer>> solve(int n, int p, int[][] arr) {
        // build graph
        // iterate over all houses
            // doing a dfs that returns the index of the last house
            // add the result
        return null;
    }
}
