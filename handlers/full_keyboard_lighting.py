from define import devices
from handlers.base import Handlers, Mode


class FullKeyboardLighting(Handlers):
    def __init__(self, mode, excluded_events=None):
        """
        :param mode: Model.Bitmap | Model.PartialBitmap
        :param excluded_events [ EventName]
        """
        super().__init__(devices.PerRGB.device_type, None, mode)
        self.excluded_events = excluded_events


def test():
    print(FullKeyboardLighting(Mode.Bitmap).data())
    print(FullKeyboardLighting(Mode.PartialBitmap, ['AMMO', 'HEALTH']).data())


if __name__ == '__main__':
    test()
