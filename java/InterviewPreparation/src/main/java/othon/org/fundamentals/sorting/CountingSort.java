package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;

@Slf4j
public class CountingSort {
    public static void main(String[] args) {
        int[] arr = new int[]{ 1, 4, 1, 2, 7, 5, 2};
        log.info("{}", arr);
        countingSort(arr);
        log.info("{}", arr);
    }

    static void countingSort(int [] arr) {
        // find the min and max to find the range. This is done
        // becasue if the array has negative values then
        // we can't use them as index
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        int range = max - min + 1;
        int[] count = new int[range];

        // count how many elements we have
        for (int i = 0; i < arr.length; i++) {
            count[arr[i]-min] += 1;
        }
        // then accumulate the count from the previous num
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }
        // then sort by assigning the value based on the ix = arr[i]-min
        // and decrease the count for that given element
        int[] output = new int[arr.length];
        for (int i = arr.length - 1; i >=0; i--) {
            int ix = arr[i] - min;
            output[count[ix] - 1] = arr[i];
            count[ix] -= 1;
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = output[i];
        };
    }
}
