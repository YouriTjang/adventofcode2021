package nl.tjang.aoc.day1

import nl.tjang.aoc.FileUtils

object Day1Part2 {
    fun depthIncreases(data: List<Int>, windowSize: Int = 2) =
         data.asSequence()
            .windowed(windowSize, 1)
            .map { it.sum() }
            .windowed(2, 1)
            .filter { it[0] < it[1] }
            .toList()
             .size
}

fun main() {
    val data = FileUtils.readFile("day1.txt")
    val result = Day1Part2.depthIncreases(data.map{ Integer.parseInt(it)}, 3)
    print(result)
}
