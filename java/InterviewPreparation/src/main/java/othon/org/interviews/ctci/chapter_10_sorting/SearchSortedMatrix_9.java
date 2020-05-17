package othon.org.interviews.ctci.chapter_10_sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;

@Slf4j
public class SearchSortedMatrix_9 {
    public static void main(String[] args) {
        int [][] matrix = new int[][] {
                {1, 4, 7, 11, 15},
          {2, 5, 8, 12, 19},
          {3, 6, 9, 16, 22},
          {10, 13, 14, 17, 24},
          {18, 21, 23, 26, 30}
        };

        Arrays.stream(matrix).forEach(i -> log.info("{}", i));
        log.info("Search {}", search(matrix, 22));
    }

    private static boolean search(int[][] matrix, int target) {
        return search(matrix, 0 , 0, matrix[0].length-1, matrix.length-1, target);
    }

    private static boolean search(int[][] matrix, int left, int up, int right, int down, int target) {
        if (left>right || up > down) {
            return false;
        }
        if (target<matrix[up][left] || target > matrix[down][right] )
            return false;
        int midColumn = (right + left) / 2;
        int row = up;
        // search for the value in the middle column in all the rows as long as not gte than target
        while (row<=down && target >= matrix[row][midColumn]) {
            if (matrix[row][midColumn] == target)
                return true;
            row +=1;
        }
        // didn't exist then search to the left or to the right
        return search(matrix, left, row,midColumn-1,down, target) || search(matrix, midColumn + 1, up,right,row-1, target);
    }
}
