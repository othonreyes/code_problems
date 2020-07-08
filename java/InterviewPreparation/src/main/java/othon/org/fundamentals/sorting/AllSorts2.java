package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;


import java.util.Arrays;

@Slf4j
public class AllSorts2 {
    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray(20, 10000);
        log.info("{}", arr);
        int[] arr2 = Arrays.copyOf(arr, arr.length);

        long startTime = System.nanoTime();
        mergeSort(arr2);
        log.info("mergeSort    {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        quickSort(arr2);
        log.info("quickSort    {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        countingSort(arr2);
        log.info("countingSort {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        insertSort(arr2);
        log.info("insertSort {}- {}", arr2, System.nanoTime() - startTime);

        int[] arr4 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        radixSort(arr4);
        log.info("radixSort    {}- {}", arr4, System.nanoTime() - startTime);

        assert Arrays.equals(arr2, arr4);
    }

    private static void radixSort(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();
        for (int exp = 1; max/exp > 0; exp *= 10) {
//            countSort(arr, arr.length, exp);
            countSort(arr, exp);
        }
    }

    private static void countSort(int[] arr, int exp) {
        int[] count = new int[10];
        for (int i = 0; i < arr.length; i++) {
            int pos = (arr[i] / exp) % 10;
            count[pos] += 1;
        }
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }
        // sort
        int[] output = new int[arr.length];
        for (int i =arr.length - 1; i >= 0 ; i--) { // this is key
        // for (int i = 0; i < arr.length; i++) {
            int pos = (arr[i] / exp) % 10;
            output[count[pos] - 1] = arr[i];
            count[pos] -= 1;
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = output[i];
        }
        log.info("{}", arr);
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
            final int pos = (arr[i] / exp) % 10;
            output[count[pos] - 1] = arr[i];
            count[pos] -= 1;
        }
        for (int i = 0; i < n; arr[i] = output[i++]);
    }

    private static void insertSort(int[] arr) {
        int i = 1;
        while (i < arr.length) {
            if (arr[i] < arr[i - 1]) {
                // need to find a new place for it.
                int j = i;
                while (j>0) {
                    if (arr[j] < arr[j - 1]) {
                        // swap
                        int temp = arr[j];
                        arr[j] = arr[j - 1];
                        arr[j - 1] = temp;
                    } else {
                        break;
                    }
                    j -= 1;
                }
            }
            i+=1;
        }
    }

    private static void countingSort(int[] arr) {
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        int range = max - min + 1 ;
        int[] count = new int[range];
        // count the items
        for (int i = 0; i < arr.length; i++) {
            int pos = arr[i] - min;
            count[pos] += 1;
        }
        // then accumulate
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }
        // then sort
        int[] output = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            int pos = arr[i] - min;
            output[count[pos]-1] = arr[i];
            count[pos] -= 1;
        }
        // copy the result
        for (int i = 0; i < arr.length; i++) {
            arr[i] = output[i];
        }
    }

    private static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right) {
        int index = partition(arr, left, right);
        if (left < index - 1) {
            quickSort(arr, left, index - 1);
        }
        if (index < right) {
            quickSort(arr, index, right);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[(left + right)/2];
        while (left<=right) {
            while(arr[left] < pivot) left++;
            while(arr[right] > pivot) right--;
            if (left<=right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left ++;
                right --;
            }
        }
        return left;
    }

    private static void mergeSort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
    }

    private static void mergeSort(int[] arr, int left, int right) {
        if (left >= right)
            return;
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int[] leftArr = Arrays.copyOfRange(arr, left, mid + 1);
        int[] rightArr = Arrays.copyOfRange(arr, mid + 1, right + 1);

        int current = left;
        int leftPointer = 0;
        int rightPointer = 0;
        while (leftPointer < leftArr.length && rightPointer < rightArr.length) {
            if (leftArr[leftPointer]<=rightArr[rightPointer]) {
                arr[current++] = leftArr[leftPointer++];
            } else {
                arr[current++] = rightArr[rightPointer++];
            }
        }
        while (leftPointer < leftArr.length) {
            arr[current++] = leftArr[leftPointer++];
        }
        while (rightPointer < rightArr.length) {
            arr[current++] = rightArr[rightPointer++];
        }
    }
}
