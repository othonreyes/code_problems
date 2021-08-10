package othon.gfg.arrays

import java.util.*

fun main() {
    val arr = intArrayOf(1, 2, 3, 4, 5, 6, 7)
    val wanted = intArrayOf(3, 4, 5, 6, 7, 1, 2)
    val positions = 2
    rotateArr(arr, positions)
    println(Arrays.toString(wanted) + " " + Arrays.toString(arr))
}

fun rotateArr(arr:IntArray, pos:Int) {
    var begining = 0
    var offset = begining + pos
    for (i in arr.size - pos until arr.size) {
        val temp = arr[begining]
        arr[begining] = arr[offset]
        arr[offset] = arr[i]
        arr[i] = temp
        begining += 1
        offset += 1
    }

    for (i in begining until arr.size - pos) {
        val temp = arr[arr.size - pos - 1]
        arr[arr.size - pos - 1] = arr[i]
        arr[i] = temp
    }
}
