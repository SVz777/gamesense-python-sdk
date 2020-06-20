# !/usr/local/bin/python3
# -*- coding: utf-8 -*-

from define import devices
from handlers.base import Data, Handlers, Mode


class Screen(Handlers):
    def __init__(self, device_type, zone, datas):
        """
        :param device_type: define.Device.device_type
        :param zone: define.Device.zone
        :param datas: StaticScreen | RangeScreen
        """
        super().__init__(device_type, zone, Mode.Screen)
        self.datas = datas


class StaticScreen(Data):
    def __init__(self, *frames):
        """
        :param frames:[ScreenFrame]
        """
        if len(frames) < 1:
            raise Exception('frames is empty')
        self.frames = frames

    def data(self):
        return [i.data() for i in self.frames]


class RangeScreen(Data):
    def __init__(self, low, high, datas):
        """
        :param low: event value, low end of range
        :param high: event value, high end of range
        :param datas: StaticScreen
        """
        self.low = low
        self.high = high
        self.datas = datas


class ScreenFrame(Data):
    pass


class SingleLineFrame(ScreenFrame):
    def __init__(self, base_data, frame_modifier=None, data_accessor=None):
        """
        :param base_data: TextModifiers | ProgressBar
        :param frame_modifier: FrameModifier
        :param data_accessor: DataAccessor
        """
        self.base_data = base_data
        if frame_modifier is not None:
            self.frame_modifier = frame_modifier
        if data_accessor is not None:
            self.data_accessor = data_accessor

    def data(self):
        m = {}
        for _, d in self.__dict__.items():
            for k, v in d.data().items():
                m[k] = v
        return m


class MultiLineFrame(ScreenFrame):
    def __init__(self, *lines, frame_modifier=None):
        """
        :param frame_modifier: FrameModifier
        :param lines: [ Line ]
        """
        if len(lines) < 1:
            raise Exception('frames is empty')
        self.frame_modifier = frame_modifier
        self.lines = lines

    def data(self):
        m = {}
        if self.frame_modifier is not None:
            for k, v in self.frame_modifier.data().items():
                m[k] = v
        m['lines'] = []
        for line in self.lines:
            m['lines'].append(line.data())
        return m


class ImageFrame(ScreenFrame):
    def __init__(self, image_data, *, frame_modifier=None):
        """
        :param frame_modifier:
        :param image_data:[ Image ]
        """
        self.has_text = False
        self.frame_modifier = frame_modifier
        self.image_data = image_data

    def data(self):
        m = {}
        if self.frame_modifier is not None:
            for k, v in self.frame_modifier.data().items():
                m[k] = v
        m['has_text'] = self.has_text
        m['image-data'] = self.image_data
        return m


class FrameModifiers(Data):
    def __init__(self, length_millis=None, icon_id=None, repeats=None):
        self.length_millis = length_millis
        self.icon_id = icon_id
        self.repeats = repeats


class Line(Data):
    def __init__(self, base_data, data_accessor=None):
        """
        :param base_data: TextModifiers | ProgressBar
        :param data_accessor: DataAccessor
        """
        self.base_data = base_data
        if data_accessor is not None:
            self.data_accessor = data_accessor

    def data(self):
        m = {}
        for _, d in self.__dict__.items():
            for k, v in d.data().items():
                m[k] = v
        return m


class TextModifiers(Data):
    def __init__(self, *, prefix='', suffix='', bold=False, wrap=0):
        self.has_text = True
        if prefix != '':
            self.prefix = prefix
        if suffix != '':
            self.suffix = suffix
        if bold:
            self.bold = bold
        if wrap != 0:
            self.wrap = wrap


class ProgressBar(Data):
    def __init__(self):
        self.has_text = False
        self.has_progress_bar = True


class DataAccessor(Data):
    def __init__(self, *, context_frame_key=None, arg=None):
        self.context_frame_key = context_frame_key
        self.arg = arg


def test():
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers()
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            RangeScreen(
                0, 15,
                TextModifiers()
            ),
            RangeScreen(
                16, 100,
                TextModifiers()
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(prefix='Got ', suffix=' kills')
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(bold=True)
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            MultiLineFrame(
                Line(
                    TextModifiers(wrap=1),
                    DataAccessor(context_frame_key='first-line')
                ),
                Line(
                    TextModifiers(),
                    DataAccessor(context_frame_key='second-line')
                )
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            MultiLineFrame(
                Line(
                    TextModifiers(prefix='Progress'),
                    DataAccessor(arg='')
                ),
                Line(
                    ProgressBar(),
                )
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(suffix='stuff'),
                FrameModifiers(icon_id=16)
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            ImageFrame(
                [0, 0, 0]
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(suffix=' kills'),
                FrameModifiers(250)
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(suffix='HeadShot!'),
                FrameModifiers(250, 7),
                DataAccessor(arg='')
            ),
            SingleLineFrame(
                TextModifiers(suffix=' kills'),
                FrameModifiers(icon_id=6)
            )
        )
    ).data())
    print(Screen(
        devices.Screen128x36.device_type,
        devices.Screen128x36.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(suffix='frame 1'),
                FrameModifiers(200)
            ),
            SingleLineFrame(
                TextModifiers(suffix='frame 2'),
                FrameModifiers(200, repeats=True)
            ),
        )
    ).data())
    print(Screen(
        devices.Screen.device_type,
        devices.Screen.zone.One,
        StaticScreen(
            SingleLineFrame(
                TextModifiers(),
                DataAccessor(arg='(custom-text: (context-frame: self))')
            ),
        )
    ).data())


if __name__ == '__main__':
    test()
