package othon.org.leetcode;

public class PathMaximumMinimumValue {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] input = {{5,4,5},{1,2,6},{7,4,6}};
        int r = s.maximumMinimumPath(input);
        System.out.println(r);

        int[][] input2 = {{2,2,1,2,2,2},{1,2,2,2,1,2}};
        r = s.maximumMinimumPath(input2);
        System.out.println(r);

        input2 = new int[][]{{2, 0, 5, 2, 0}, {2, 4, 4, 4, 3}, {1, 5, 0, 0, 0}, {5, 4, 4, 3, 1}, {1, 3, 1, 5, 3}};
        r = s.maximumMinimumPath(input2);
        System.out.println(r);
    }

    static class Solution {
        public int maximumMinimumPath(int[][] A) {
            boolean[][] visited = new boolean[A.length][A[0].length];
            return explore(A, A.length - 1, A[0].length -1, Integer.MAX_VALUE, visited);
        }

        int explore(int[][]A, int y, int x, Integer minValue, boolean[][] visited) {
            log("A[y,z]= A["+y+","+x+"]="+A[y][x]);
            if (y == 0 && x == 0) {
                minValue = minValue == null ? Integer.MAX_VALUE: minValue;
                return Math.min(minValue, A[y][x]);
            }
            visited[y][x] = true;
            int down = y + 1 < A.length && !visited[y + 1][x]? A[y + 1][x] : Integer.MIN_VALUE;
            int up = y - 1 >= 0 && !visited[y - 1][x]? A[y - 1][x] : Integer.MIN_VALUE;

            int right = x + 1 < A[0].length && !visited[y][x + 1]? A[y][x + 1] : Integer.MIN_VALUE;
            int left = x - 1 >= 0 && !visited[y][x - 1]? A[y][x - 1] : Integer.MIN_VALUE;

            int max = Math.max(Math.max(up, down),Math.max(left, right));

            if (max == up) {
                log("UP->"+(y-1)+","+x);
                return explore(A, y - 1, x, Math.min(minValue, A[y][x]), visited);
            } else if (max == left) {
                log("LEFT->"+y+","+(x-1));
                return explore(A, y, x - 1, Math.min(minValue, A[y][x]), visited);
            } else if (max == down) {
                log("DOWN->"+(y+1)+","+x);
                return explore(A, y + 1, x, Math.min(minValue, A[y][x]), visited);
            } else {
                log("RIGHT->"+y+","+(x+1));
                return explore(A, y, x + 1, Math.min(minValue, A[y][x]), visited);
            }
        }
    }
     static void log(String s) {
        System.out.println(s);
     }
}
