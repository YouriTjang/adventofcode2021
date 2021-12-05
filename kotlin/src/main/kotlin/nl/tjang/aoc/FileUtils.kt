package nl.tjang.aoc

object FileUtils {
    fun readFile(fileName: String): List<String> {
        val gotoResources = "../../../"
        return FileUtils::class.java.getResourceAsStream("$gotoResources$fileName").bufferedReader().readLines()
    }
}