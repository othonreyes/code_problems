//https://www.hackerrank.com/challenges/equality-in-a-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

fun equalize(arr:List<Int>):Int {
    val map = mutableMapOf<Int, Int>()

    for (a in arr) {
        map[a] = map.getOrDefault(a, 0) + 1
    }
    var count = 0
    for (e in map) {
        if (e.value > count) {
            count = e.value
        }
    }
    return arr.size - count
}
