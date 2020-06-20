import json

from define import devices
from handlers.base import Data, Handlers, Mode


class Color(Handlers):
    def __init__(self, device_type, zone, mode, color, custom_zone_keys, rate=None):
        """
        :param device_type: define.Device.device_type
        :param zone: define.Device.zone
        :param mode: Mode
        :param color: StaticColor | GradientColor
        :param custom_zone_keys: https://www.usb.org/document-library/hid-usage-tables-112
        :param rate: Rate
        """
        super().__init__(device_type, zone, mode)
        self.custom_zone_keys = custom_zone_keys
        self.color = color
        self.rate = rate


class StaticColor(Data):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class GradientColor(Data):
    def __init__(self, zero, hundred):
        """
        :param zero: StaticColor
        :param hundred: StaticColor
        """
        self.zero = zero
        self.hundred = hundred

    def data(self):
        m = {}
        for k, v in self.__dict__.items():
            if isinstance(v, Data):
                m[k] = v.data()
            else:
                m[k] = v
        return {'gradient': m}


class RangeColor(Data):
    def __init__(self, low, high, color):
        """
        :param low: event value, low end of range
        :param high: event value, high end of range
        :param color: StaticColor | GradientColor
        """
        self.low = low
        self.high = high
        self.color = color


def test():
    r = Color(
        devices.PerRGB.device_type,
        devices.PerRGB.zone.GroupMacroKeys,
        None,
        Mode.Color,
        StaticColor(255, 0, 0))
    print(json.dumps(r.data()))


if __name__ == '__main__':
    test()
