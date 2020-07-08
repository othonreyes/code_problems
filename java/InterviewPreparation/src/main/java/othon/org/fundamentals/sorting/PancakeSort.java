package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;

import java.util.Arrays;

@Slf4j
public class PancakeSort {
    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray(10, 100);
        log.info("{}", arr);

        int[] arr2 = Arrays.copyOf(arr, arr.length);
        long startTime = System.nanoTime();
        pacakeSort(arr2);
        log.info("[{}ns]{}", System.nanoTime() - startTime, arr2);
    }

    private static void pacakeSort(int[] arr) {
        int current = arr.length -1;
        while (current >= 0) {
            // find the max
            int max = arr[0];
            int maxIx = 0;
            for (int i = 1; i <= current ; i++ ) {
                if (arr[i] > max) {
                    max = arr[i];
                    maxIx = i;
                }
            }
            int temp = arr[current];
            arr[current] = max;
            arr[maxIx] = temp;
            current -= 1;
        }
    }
}
