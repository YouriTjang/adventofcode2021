package nl.tjang.aoc.day2

import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

internal class Day2Part1Test {

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
        val d = Day2Part1()
        assertEquals(150, d.doThings(data))
    }


}