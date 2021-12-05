package nl.tjang.aoc.day2

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class Day2Part2Test {
    @Test
    fun testThings() {
        val data = listOf(
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        )
        val d = Day2Part2()
        assertEquals(900, d.doThings(data))
    }
}