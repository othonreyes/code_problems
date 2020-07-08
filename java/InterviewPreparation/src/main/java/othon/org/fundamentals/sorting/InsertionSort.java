package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;

import java.util.Arrays;

@Slf4j
public class InsertionSort {

    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray();
        log.info("{}", arr);

        int[] arr2 = Arrays.copyOf(arr, arr.length);
        long startTime = System.nanoTime();
        insertionSort(arr2);
        log.info("insertionSort {}- {}", arr2, System.nanoTime() - startTime);
    }

    private static void insertionSort(int arr[]) {
        int i = 1;
        while ( i < arr.length) {
            // if the current element is not ordered
            if (arr[i]<arr[i-1]) {
                int j = i;
                int temp = arr[i];
                // swap the elements
                while (j>0 && arr[j]<arr[j-1]) {
                    temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                    j -=1;
                }
                arr[j] = temp;
            }
            i +=1;
        }
    }

}
