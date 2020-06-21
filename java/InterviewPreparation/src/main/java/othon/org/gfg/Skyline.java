package othon.org.gfg;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * https://www.geeksforgeeks.org/the-skyline-problem-using-divide-and-conquer-algorithm/
 */
public class Skyline {
    public static void main(String[] args) {

    }

    static class Solution {
        List<List<Integer>> getSkyline(int[][] skyline) {
            int n = skyline.length;
            List<List<Integer>> output = new ArrayList<>();
            if (n==0) return output;
            if (n==1) {
                int l = skyline[0][0];
                int h = skyline[0][1];
                int r = skyline[0][2];
                output.add(Arrays.asList(l,h));
                output.add(Arrays.asList(r,0));
                return output;
            }
            int m = n /2;
            List<List<Integer>> left = getSkyline(Arrays.copyOfRange(skyline, 0, m + 1));
            List<List<Integer>> right = getSkyline(Arrays.copyOfRange(skyline, m + 1, n + 1));
            return merge(left, right);
        }

        private List<List<Integer>> merge(List<List<Integer>> left, List<List<Integer>> right) {
            int pl = 0;int pr = 0; int nL = left.size(); int nR = right.size();
            int currY = 0, leftY = 0, rightY=0, maxY = 0;
            int x = 0;
            List<List<Integer>> output = new ArrayList<>();
            while (pl < nL && pr<nR) {
                // pick the smaller x
                if (left.get(pl).get(0)< right.get(pr).get(0)) {
                    x = left.get(pl).get(0);
                    leftY = left.get(pl).get(1);
                    pl += 1;
                } else {
                    x = left.get(pl).get(0);
                    rightY = left.get(pl).get(1);
                    pr += 1;
                }
                maxY = Math.max(leftY, rightY);
                if (currY != maxY) {
                    updateOutput(output, x, maxY);
                    currY = maxY;
                }
            }
            appendSkyline(output, left, pl, currY);
            appendSkyline(output, right, pr, currY);
            return output;
        }

        private void updateOutput(List<List<Integer>> output, int x, int y) {
            if (output.isEmpty() || output.get(output.size()-1).get(0) != x) {
                output.add(Arrays.asList(x, y));
            } else {
                output.get(output.size()-1).set(1, y);
            }
        }

        private void appendSkyline(List<List<Integer>> output, List<List<Integer>> left, int pl, int currY) {
            for (int i = pl; i < left.size(); i++) {
                int x = left.get(i).get(1);
                int y = left.get(i).get(1);
                if (currY != y) {
                    updateOutput(output, x, y);
                    currY = y;
                }
            }
        }
    }
}
