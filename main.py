"""
We are up to here -> https://python-tcod.readthedocs.io/en/latest/tutorial/part-03.html#new-globals
Here are some good assets -> https://free-game-assets.itch.io/ also at https://craftpix.net/freebies/free-pixel-art-tiny-hero-sprites/ but you need an account
This is the old toutorial -> https://www.rogueliketutorials.com/tutorials/tcod/v2
Here are some fonts -> https://github.com/libtcod/python-tcod/blob/11.13.5/fonts/libtcod
This github repo's url -> https://github.com/Ghostboo124/tcod-test
"""

from __future__ import annotations

import attrs

import g
import game.states
import game.world_tools

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    console = tcod.console.Console(80, 50)
    state = game.states.InGame()
    g.world = game.world_tools.new_world()

    with tcod.context.new(console=console, tileset=tileset) as g.context:
        while True:
            console.clear()
            state.on_draw(console)
            g.context.present(console)
            for event in tcod.event.wait():
                #print(event)
                state.on_event(event)

if __name__ == "__main__":
    main()