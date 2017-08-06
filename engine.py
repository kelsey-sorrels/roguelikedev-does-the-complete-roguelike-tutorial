import libtcodpy as libtcod
from input_handlers import handle_keys
from entity import Entity, get_blocking_entities_at_location
from render_function import render_all, clear_all
from map_objects.game_map import GameMap
from fov_functions import initialize_fov, recompute_fov
from game_states import GameStates

#fonction main Check if the module is ran as main program (name devient main).
#Si ce fichier est importé d'un autre module, name sera le nom du module
def main():
#Carac de l'écran
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
#Minimum de la room
    room_max_size = 15
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 1
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3


    colors = {
        'dark_wall': libtcod.Color(128, 128, 128),
        'dark_ground': libtcod.Color(0, 0, 0),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }


    player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True)
    entities = [player]


    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
#What create the screen (Width, Height, Nom, Fullscreen)
    libtcod.console_init_root(screen_width, screen_height, 'Eolandia', False)
#Console principale?
    con = libtcod.console_new(screen_width, screen_height)
#Initialise la Game map
    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities, max_monsters_per_room)

    fov_recompute = True
    fov_map = initialize_fov(game_map)


    key = libtcod.Key()
    mouse = libtcod.Mouse()

    game_state = GameStates.PLAYERS_TURN
#boucle qui se finit pas
    while not libtcod.console_is_window_closed():
#Function that capture new event
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
#Function that draws entities
        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)

        fov_recompute = False

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

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy

            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)
                if target:
                    print('You kick the ' + target.name + ' in the shins, much to its annoyance!')
                else:
                    player.move(dx, dy)

                    fov_recompute = True
                game_state = GameStates.ENEMY_TURN
        if exiting:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity != player:
                    print('The' + entity.name + ' ponders the meaning of its existence')

            game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    main()
