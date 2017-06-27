import libtcodpy as libtcod
from input_handlers import handle_keys

#fonction main Check if the module is ran as main program (name devient main).
#Si ce fichier est importé d'un autre module, name sera le nom du module
def main():
#Carac de l'écran
    screen_width = 80
    screen_height = 50
    player_x = int(screen_width /2)
    player_y = int(screen_height /2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
#What create the screen (Width, Height, Nom, Fullscreen)
    libtcod.console_init_root(screen_width, screen_height, 'Eolandia', False)
#Console principale?
    con = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()
#boucle qui se finit pas
    while not libtcod.console_is_window_closed():
#Function that capture new event
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
#Font
        libtcod.console_set_default_foreground(con, libtcod.purple)
#coordonées du perso (La console, x, y, char, print+bckgrd rien)
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()

        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)
#Partie pour bouger. Apelle le fichier Handle keys.
#Return des dictionary.Ces valeurs vont dans la variable action
#Action contiendras des clés (move, exit, or fullscre)
        action = handle_keys(key)

        move = action.get('move')
        exiting = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        elif exiting:
            return True

        elif fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
