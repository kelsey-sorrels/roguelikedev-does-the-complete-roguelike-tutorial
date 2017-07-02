package com.malcolmcrum.roguelike

import asciiPanel.AsciiPanel
import javax.swing.JFrame

fun main(args: Array<String>) {
    val main = Main()
    main.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
    main.isVisible = true
}

class Main : JFrame() {

    val terminal: AsciiPanel = AsciiPanel()

    init {
        terminal.write("rl tutorial", 1, 1)
        add(terminal)
        pack()
    }

}