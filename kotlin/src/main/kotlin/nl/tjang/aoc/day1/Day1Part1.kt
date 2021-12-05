package nl.tjang.aoc.day1

import nl.tjang.aoc.FileUtils

object Day1Part1 {
    fun depthIncreases(data: List<Int>): Int =
        data.asSequence()
            .windowed(2, 1)
            .filter { it[0] < it[1] }
            .toList()
            .size
}

fun main() {
    val data = FileUtils.readFile("day1.txt")
    val result = Day1Part1.depthIncreases(data.map{ Integer.parseInt(it)})
    print(result)
}