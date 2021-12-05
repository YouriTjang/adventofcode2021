package nl.tjang.aoc.day2

import nl.tjang.aoc.FileUtils

data class Position(
    val x: Int = 0,
    val y: Int = 0,
) {
    operator fun plus(that: Position): Position {
        return Position(this.x + that.x, this.y + that.y)
    }

    fun vector() = x * y
}

class Day2Part1 {
    fun doThings(data: List<String>): Int =
        data.map { it.split(" ") }
            .map(this::mapToAction)
            .reduce(Position::plus)
            .vector()

    private fun mapToAction(it: List<String>) = when (it[0]) {
        "forward" -> Position(it[1].toInt(), 0)
        "up" -> Position(0, -it[1].toInt())
        "down" -> Position(0, it[1].toInt())
        else -> Position()
    }
}

fun main() {
    val data = FileUtils.readFile("day2.txt")
    val result = Day2Part1().doThings(data)
    print(result)
}