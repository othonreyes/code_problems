package othon.org.fundamentals.misc;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;

import java.util.Arrays;

/* TODO:
 * heap
 * - as a tree
 * - extract min
 */

@Slf4j
public class Heaps {

    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedUniqueElemArray(10, 100);
        log.info("{}", arr);
        int[] arr2 = Arrays.copyOfRange(arr, 0, arr.length);
        Heap heap = new Heap();
        heap.minHeap(arr2);
        log.info("{}", arr2);
        arr2 = Arrays.copyOfRange(arr, 0, arr.length);
        heap.heapSort(arr2);
        log.info("{}", arr2);
    }

    static class Heap {

        void heapSort(int[] arr) {
            for (int i = arr.length; i > 0; i--) {
                maxHeap(arr, i);
                int temp = arr[i - 1];
                arr[i - 1] = arr[0];
                arr[0] = temp;
            }
        }

        void maxHeap(int[] arr, int n) {
            int start = n / 2 - 1;
            for (int i = start; i >=0; i--) {
                maxHeapify(arr, i, n);
            }
        }

        private void maxHeapify(int[] arr, int i, int n) {
            int largest = i;
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            if (left < n && arr[largest] < arr[left]) {
                largest = left;
            }
            if (right < n && arr[largest] < arr[right]) {
                largest = right;
            }
            if (largest != i) {
                // swap
                int temp = arr[largest];
                arr[largest] = arr[i];
                arr[i] = temp;
                maxHeapify(arr, largest, n);
            }
        }

        void minHeap(int[] arr) {
            int n  = arr.length;
            minHeap(arr, n);
        }

        void minHeap(int[] arr, int n) {
            int start = n / 2 - 1;
            for (int i = start; i >=0; i--) {
                minHeapify(arr, i, n);
            }
        }

        private void minHeapify(int[] arr, int i, int n) {
            int smallest = i;
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            if (left <n && arr[smallest] > arr[left]) {
                smallest = left;
            }
            if (right <n && arr[smallest] > arr[right]) {
                smallest = right;
            }
            if (smallest != i) {
                // swap
                int temp = arr[smallest];
                arr[smallest] = arr[i];
                arr[i] = temp;
                minHeapify(arr, smallest, n);
            }
        }
    }
}
