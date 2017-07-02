import libtcodpy as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_function import render_all, clear_all
from map_objects.game_map import GameMap

#fonction main Check if the module is ran as main program (name devient main).
#Si ce fichier est importé d'un autre module, name sera le nom du module
def main():
#Carac de l'écran
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }


    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.purple)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
#What create the screen (Width, Height, Nom, Fullscreen)
    libtcod.console_init_root(screen_width, screen_height, 'Eolandia', False)
#Console principale?
    con = libtcod.console_new(screen_width, screen_height)
#Initialise la Game map
    game_map = GameMap(map_width, map_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()
#boucle qui se finit pas
    while not libtcod.console_is_window_closed():
#Function that capture new event
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

#Function that draws entities
        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
#Clear les entities pour que ça ne laisse pas de traces
        clear_all(con, entities)
#Partie pour bouger. Apelle le fichier Handle keys.
#Return des dictionary.Ces valeurs vont dans la variable action
#Action contiendras des clés (move, exit, or fullscre)
        action = handle_keys(key)

        move = action.get('move')
        exiting = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        elif exiting:
            return True

        elif fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
