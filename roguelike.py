import tdl


# actual size of the window
_SCREEN_WIDTH = 80
_SCREEN_HEIGHT = 50
_LIMIT_FPS = 20


def handle_keys():
    global playerx, playery

    # user_input = tdl.event.key_wait()
    # realtime
    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
            user_input = event
            keypress = True
    if not keypress:
        return

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())
    # exit the game
    elif user_input.key == 'ESCAPE':
        return True

    # movement keys
    if user_input.key == 'UP':
        playery -= 1
    elif user_input.key == 'DOWN':
        playery += 1
    elif user_input.key == 'LEFT':
        playerx -= 1
    elif user_input.key == 'RIGHT':
        playerx += 1

tdl.set_font('consolas12x12_gs_tc.png', greyscale=True, altLayout=True)
console = tdl.init(_SCREEN_WIDTH,
                   _SCREEN_HEIGHT,
                   title='Roguelike',
                   fullscreen=False)
# setting fps is not needed if turn-based
tdl.setFPS(_LIMIT_FPS)


playerx = _SCREEN_WIDTH // 2
playery = _SCREEN_HEIGHT // 2

while not tdl.event.is_window_closed():
    console.draw_char(x=playerx,
                      y=playery,
                      char='@',
                      bg=None,
                      fg=(255, 255, 255))
    tdl.flush()

    console.draw_char(x=playerx, y=playery, char=' ', bg=None)

    # handle keys and exit game if needed
    exit_game = handle_keys()
    if exit_game:
        break

