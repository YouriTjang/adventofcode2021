package nl.tjang.aoc.day2

import nl.tjang.aoc.FileUtils

data class PositionAim(
    val x: Int = 0,
    val y: Int = 0,
    val aim: Int = 0,
) {
    operator fun plus(that: PositionAim): PositionAim {
        return PositionAim(this.x + that.x, this.y + that.y, this.aim + that.aim)
    }
    fun forward(x: Int): PositionAim {
        return PositionAim(this.x + x, this.y + this.aim * x, this.aim)
    }

    fun vector() = x * y
}

class Day2Part2 {
    fun doThings(data: List<String>): Int {
        return data.map { it.split(" ") }
            .fold(PositionAim()){ acc, next -> mapToAction(acc, next) }
            .vector()
    }

    private fun mapToAction(acc: PositionAim, it: List<String>): PositionAim {
        return when (it[0]) {
            "forward" -> acc.forward(it[1].toInt())
            "up" -> acc.plus(PositionAim(0, 0, -it[1].toInt()))
            "down" -> acc.plus(PositionAim(0, 0, it[1].toInt()))
            else -> PositionAim()
        }
    }
}

fun main() {
    val data = FileUtils.readFile("day2.txt")
    val result = Day2Part2().doThings(data)
    print(result)
}