package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;

@Slf4j
public class RadixSort {
    /*Driver function to check for above function*/
    public static void main (String[] args)
    {
        int[] arr = SortingUtils.createUnorderedArray(20, 10000);
        int n = arr.length;
        radixsort(arr, n);
        log.info("{}", arr);
    }

    private static void radixsort(int[] arr, int n) {
        int max = Arrays.stream(arr).max().getAsInt();
        for (int exp = 1; max/exp > 0 ; exp *= 10) {
            countSort(arr, arr.length, exp);
            log.info("{}", arr);
        }
    }

    private static void countSort(int[] arr, int n, int exp) {
        int[] count = new int[10];
        for (int i = 0; i < n; i++) {
            // divide by the exponent
            // and obtain the modulus of the output to find the position in count
            count[ (arr[i]/exp) % 10 ] += 1;
        }
        for (int i = 1; i < count.length; count[i] += count[i++ - 1]);
        int[] output = new int[n];
        for (int i = n - 1; i >= 0 ; i--) {
            output[count[ (arr[i]/exp) % 10 ] - 1] = arr[i];
            count[ (arr[i]/exp) % 10 ] -= 1;
        }
        for (int i = 0; i < n; arr[i] = output[i++]);
    }

}
