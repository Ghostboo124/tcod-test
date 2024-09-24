"""
We are up to here -> https://python-tcod.readthedocs.io/en/latest/tutorial/part-02.html#new-ingame-state
Here are some good assets -> https://free-game-assets.itch.io/ also at https://craftpix.net/freebies/free-pixel-art-tiny-hero-sprites/ but you need an account
This is the old toutorial -> https://www.rogueliketutorials.com/tutorials/tcod/v2
Here are some fonts -> https://github.com/libtcod/python-tcod/blob/11.13.5/fonts/libtcod
This github repo's url -> https://github.com/Ghostboo124/tcod-test
"""

from __future__ import annotations

import attrs

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


@attrs.define()
class ExampleState:
    player_x: int = 0
    player_y: int = 0

    def on_draw(self, console: tcod.console.Console) -> None:
        console.print(self.player_x, self.player_y, "@")

    def on_event(self, console: tcod.console.Console, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_x <= 0:
                    pass
                else:
                    self.player_x -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_x >= console.width - 1:
                    pass
                else:
                    self.player_x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_y <= 0:
                    pass
                else:
                    self.player_y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_y >= console.height - 1:
                    pass
                else:
                    self.player_y += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.a):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_x <= 0:
                    pass
                else:
                    self.player_x -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.d):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_x >= console.width - 1:
                    pass
                else:
                    self.player_x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.w):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_y <= 0:
                    pass
                else:
                    self.player_y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.s):
                print("Console width:", console.width)
                print("Console height:", console.height)
                print("Player x:", self.player_x)
                print("Player y:", self.player_y)
                if self.player_y >= console.height - 1:
                    pass
                else:
                    self.player_y += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.ESCAPE):
                raise SystemExit

def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    console = tcod.console.Console(80, 50)
    state = ExampleState(player_x=console.width // 2, player_y=console.height // 2)

    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:
            console.clear()
            state.on_draw(console)
            context.present(console)
            for event in tcod.event.wait():
                #print(event)
                state.on_event(console, event)

if __name__ == "__main__":
    main()