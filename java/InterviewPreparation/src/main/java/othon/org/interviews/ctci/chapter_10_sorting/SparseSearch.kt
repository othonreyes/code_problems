package othon.org.interviews.ctci.chapter_10_sorting

fun main() {
    val arr = arrayOf( "at", "", "", "", "ball", "", "","car", "", "", "", "dad", "", "", "")
    println(search("at", arr))
    println(search("cheeto", arr))
}

private fun search(s: String, arr: Array<String>): Int {
    var left = 0
    var right = arr.size
    while (left<right) {
        var middle = (right + left) / 2
        var newLeft = middle
        var newRight = middle
        while (arr[newLeft].equals("") && arr[newRight].equals("") && newLeft > left && newRight < right) {
            newRight += 1
            newLeft -= 1
        }
        if (!arr[newLeft].equals(""))
            middle = newLeft
        else
            middle = newRight
        if (arr[middle].equals(s)) {
            return middle
        }
        if (arr[middle].compareTo(s) == -1) {
            left = middle + 1
        } else {
            right = middle - 1
        }
    }
    return -1
}
