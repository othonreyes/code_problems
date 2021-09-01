package othon.hackerrank

fun main() {
    println(6 == jumpClouds(listOf(0,0,1,0,0,0,0,1,0,0)))
}

fun jumpClouds(c:List<Int>):Int {
    val dp = IntArray(c.size) { Int.MAX_VALUE }
    return minSteps(c, dp, c.size -1)
}

/** Problems:
 * Took 1:40hr to resolve the problem using dp.
 */
fun minSteps(c:List<Int>, dp:IntArray, ix:Int):Int {
    if (ix < 0 || c[ix] == 1) {
        return Int.MAX_VALUE
    }
    if (ix == 0) {
        return ix
    }
    if (dp[ix] != Int.MAX_VALUE) {
        return dp[ix]
    }
    val left = minSteps(c, dp, ix - 1).let { if (it != Int.MAX_VALUE) it + 1 else it }
    val right = minSteps(c, dp, ix - 2).let { if (it != Int.MAX_VALUE) it + 1 else it }
    println("[$ix]left=$left vs right=$right")
    dp[ix] = Math.min(left, right)
    return dp[ix]
}

fun jumpClouds2(c:List<Int>):Int {
    var jumps = -1
    var i = 0
    while (i < c.size) {
        if (i<c.size-2 && c[i + 2]==0) {
            i+=1
        }
        jumps += 1
        i+=1
    }
    return jumps
}

fun jumpClouds3(c:List<Int>):Int {
    return jumpRec(c, c.size - 1)
}

fun jumpRec(c:List<Int>, ix:Int):Int {
    if (ix == 0) return 1
    if (ix > 1 && c[ix-2]==0)
        return jumpRec(c, ix - 2) + 1
    return jumpRec(c, ix-1) + 1
}
