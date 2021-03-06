import time

from define import devices
from game_sense import GameSense
from handlers import screen, tactile

gs = GameSense('SVZ_TEST')
gs.remove_game()
gs.register_game('svz', developer='svz')


def test1():
    print(gs.bind_game_event('T1', handlers=[
        screen.Screen(
            devices.Screen128x36.device_type,
            devices.Screen128x36.zone.One,
            screen.StaticScreen(
                screen.SingleLineFrame(
                    screen.TextModifiers()
                )
            )
        )
    ]))
    gs.send_game_event(
        'T2', {
            'value': 10,
        })


def test2():
    print(gs.bind_game_event('T2', handlers=[
        screen.Screen(
            devices.Screen128x36.device_type,
            devices.Screen128x36.zone.One,
            screen.StaticScreen(
                screen.SingleLineFrame(
                    screen.TextModifiers(suffix=' K'),
                    screen.FrameModifiers(1000, icon_id=6)
                ),
                screen.SingleLineFrame(
                    screen.TextModifiers(),
                    screen.FrameModifiers(1000, repeats=True),
                    screen.DataAccessor(arg='(time: (context-frame: self))')
                )
            )
        ),
        tactile.Tactile(
            tactile.StaticPattern(
                tactile.PredefinedPattern(
                    tactile.PredefinedPatternType.TiPredefinedStrongClick100
                )
            )
        )
    ]))
    gs.send_game_event(
        'T2', {
            'value': 10, 'frame': {
                'time': time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime())
            }
        })


def test3():
    print(gs.bind_game_event('T3', handlers=[
        screen.Screen(
            devices.Screen128x36.device_type,
            devices.Screen128x36.zone.One,
            screen.StaticScreen(
                screen.ImageFrame(
                    [0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     8,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     12,
                     0,
                     0,
                     0,
                     0,
                     28,
                     0,
                     0,
                     28,
                     0,
                     0,
                     0,
                     112,
                     0,
                     0,
                     0,
                     12,
                     0,
                     0,
                     0,
                     4,
                     28,
                     0,
                     0,
                     28,
                     0,
                     0,
                     0,
                     112,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     14,
                     28,
                     0,
                     0,
                     28,
                     0,
                     0,
                     0,
                     112,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     4,
                     127,
                     0,
                     120,
                     28,
                     7,
                     0,
                     112,
                     112,
                     224,
                     14,
                     0,
                     0,
                     28,
                     1,
                     128,
                     1,
                     255,
                     193,
                     254,
                     127,
                     31,
                     193,
                     252,
                     115,
                     248,
                     63,
                     140,
                     236,
                     127,
                     15,
                     224,
                     1,
                     193,
                     195,
                     207,
                     127,
                     63,
                     227,
                     254,
                     119,
                     28,
                     113,
                     207,
                     236,
                     227,
                     156,
                     112,
                     3,
                     128,
                     227,
                     135,
                     28,
                     112,
                     119,
                     6,
                     118,
                     12,
                     96,
                     207,
                     12,
                     193,
                     152,
                     48,
                     3,
                     28,
                     99,
                     192,
                     28,
                     112,
                     119,
                     7,
                     119,
                     0,
                     192,
                     108,
                     13,
                     128,
                     216,
                     0,
                     31,
                     54,
                     113,
                     248,
                     28,
                     112,
                     119,
                     7,
                     115,
                     192,
                     192,
                     108,
                     13,
                     128,
                     223,
                     0,
                     63,
                     34,
                     112,
                     254,
                     28,
                     127,
                     247,
                     255,
                     113,
                     248,
                     255,
                     236,
                     13,
                     255,
                     199,
                     224,
                     31,
                     54,
                     112,
                     31,
                     28,
                     127,
                     247,
                     255,
                     112,
                     28,
                     192,
                     12,
                     13,
                     128,
                     0,
                     112,
                     3,
                     28,
                     96,
                     7,
                     28,
                     112,
                     7,
                     0,
                     112,
                     14,
                     192,
                     12,
                     13,
                     128,
                     0,
                     56,
                     3,
                     128,
                     227,
                     131,
                     28,
                     112,
                     119,
                     7,
                     118,
                     6,
                     224,
                     108,
                     13,
                     192,
                     216,
                     24,
                     3,
                     193,
                     227,
                     199,
                     31,
                     63,
                     227,
                     254,
                     119,
                     14,
                     112,
                     204,
                     12,
                     225,
                     156,
                     48,
                     1,
                     247,
                     193,
                     254,
                     31,
                     31,
                     193,
                     252,
                     115,
                     252,
                     63,
                     140,
                     12,
                     127,
                     15,
                     240,
                     0,
                     255,
                     128,
                     124,
                     31,
                     7,
                     0,
                     112,
                     112,
                     240,
                     14,
                     12,
                     12,
                     28,
                     3,
                     128,
                     0,
                     28,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0,
                     0],
                )
            )
        )
    ]))
    img = [255, 255, 255, 255]
    img.extend([0 for _ in range(576 - len(img))])
    gs.send_game_event(
        'T3', {
            'value': 1,
            'frame': {
                'image-data-128x36': img
            }
        })


def test4():
    print(gs.bind_game_event('T4', handlers=[
        screen.Screen(
            devices.Screen128x36.device_type,
            devices.Screen128x36.zone.One,
            screen.StaticScreen(
                screen.SingleLineFrame(
                    screen.ProgressBar()
                )
            )
        )
    ]))
    gs.send_game_event(
        'T4', {
            'value': 40,
        })


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
