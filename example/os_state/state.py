import time

import psutil

from define import devices
from game_sense import GameSense
from handlers import screen, tactile

EVENT_NAME = 'PERCENT'
APP_NAME = 'SVZ'
SHOW_NAME = "svz's os stats"
DEVELOPER = 'svz'
gs = GameSense(APP_NAME)


def init():
    print(gs.register_game(SHOW_NAME, developer=DEVELOPER))
    print(gs.bind_game_event(EVENT_NAME, value_optional=True, handlers=[
        screen.Screen(
            devices.Screen128x36.device_type,
            devices.Screen128x36.zone.Screen128x36,
            screen.StaticScreen(
                screen.SingleLineFrame(
                    screen.TextModifiers(
                        prefix='cpu: ',
                        suffix='%',
                    ),
                    screen.FrameModifiers(
                        length_millis=1000,
                    )
                ),
                screen.SingleLineFrame(
                    screen.TextModifiers(
                        prefix='mem: ',
                        suffix='%',
                    ),
                    screen.FrameModifiers(
                        length_millis=1000,
                    ),
                    screen.DataAccessor(
                        context_frame_key='mem'
                    )
                )
            )
        )]))


def loop():
    while True:
        data = {
            'value': psutil.cpu_percent(),
            'frame': {
                'mem': psutil.virtual_memory().percent
            }
        }
        print(gs.send_game_event(EVENT_NAME, data))
        time.sleep(2)


if __name__ == '__main__':
    init()
    loop()
