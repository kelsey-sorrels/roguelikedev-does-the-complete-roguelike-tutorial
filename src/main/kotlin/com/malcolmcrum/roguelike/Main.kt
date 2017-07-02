package com.malcolmcrum.roguelike

import asciiPanel.AsciiPanel
import mu.KotlinLogging
import java.awt.event.KeyEvent
import java.awt.event.KeyListener
import javax.swing.JFrame

fun main(args: Array<String>) {
    log.info { "Starting Roguelike..." }
    val main = Main()
    main.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
    main.isVisible = true
    log.info { "Roguelike initialized." }
}

private val log = KotlinLogging.logger {}

class Main : JFrame(), KeyListener {

    private val terminal: AsciiPanel = AsciiPanel()
    private var playerX: Int
    private var playerY: Int


    init {
        terminal.write("rl tutorial", 1, 1)
        add(terminal)
        playerX = terminal.widthInCharacters/2
        playerY = terminal.heightInCharacters/2
        pack()
        addKeyListener(this)
        repaint()
    }

    override fun repaint(time: Long, x: Int, y: Int, width: Int, height: Int) {
        terminal.clear()
        terminal.write('@', playerX, playerY)
        log.debug { "Painted player at $playerX, $playerY" }
        terminal.repaint()
    }

    override fun keyPressed(e: KeyEvent?) {
        log.debug { "Received key pressed: ${e?.keyCode}" }
        when (e?.keyCode) {
            KeyEvent.VK_UP -> playerY--
            KeyEvent.VK_DOWN -> playerY++
            KeyEvent.VK_LEFT -> playerX--
            KeyEvent.VK_RIGHT -> playerX++
        }
        repaint()
    }

    override fun keyReleased(e: KeyEvent?) {}

    override fun keyTyped(e: KeyEvent?) {}

}