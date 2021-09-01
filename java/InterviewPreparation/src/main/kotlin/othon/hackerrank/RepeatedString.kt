package othon.code_problems.hackerrank

fun main() {
    val result = 7L
    println(result == repeatedAs("aba", 10L))
}

fun repeatedAs(s: String, n: Long): Long {
    val srepeated = n / s.length
    var totalAs = 0L
    for (i in 0..s.length)
        if (s[i] == 'a')
            totalAs += 1
    var repeatedAs = srepeated * totalAs;
    if (n%s.length > 0) {
        val n2 = n - srepeated * s.length
        for (i in 0..n2)
            if (s[i.toInt()] == 'a')
                repeatedAs += 1
    }
    return repeatedAs

}
