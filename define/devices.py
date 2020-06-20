from define import zones


class Device:
    device_type = ''
    zone = zones.Zone
    pass


class General(Device):
    pass


class Keyboard(General):
    device_type = 'keyboard'
    zone = zones.Keyboard


class Mouse(General):
    device_type = 'mouse'
    zone = zones.Mouse


class HeadSet(General):
    device_type = 'headset'
    zone = zones.Headset


class Indicator(General):
    device_type = 'Indicator'
    zone = zones.Indicator


class ZonedRGB(Device):
    device_type = 'rgb-zoned-device'
    zone = zones.ZonedRGB


class ZonedRGB1(ZonedRGB):
    device_type = 'rgb-1-zone'


class ZonedRGB2(ZonedRGB):
    device_type = 'rgb-2-zone'


class ZonedRGB3(ZonedRGB):
    device_type = 'rgb-3-zone'


class ZonedRGB5(ZonedRGB):
    device_type = 'rgb-5-zone'


class ZonedRGB8(ZonedRGB):
    device_type = 'rgb-8-zone'


class ZonedRGB12(ZonedRGB):
    device_type = 'rgb-12-zone'


class ZonedRGB17(ZonedRGB):
    device_type = 'rgb-17-zone'


class ZonedRGB24(ZonedRGB):
    device_type = 'rgb-24-zone'


class ZonedRGB103(ZonedRGB):
    device_type = 'rgb-103-zone'


class PerRGB(Device):
    device_type = 'rgb-per-key-zones'
    zone = zones.PerRGB


class Tactile(Device):
    device_type = 'tactile'
    zone = zones.Tactile


class Screen(Device):
    device_type = 'screened'
    zone = zones.Screen


class Screen128x36(Screen):
    device_type = 'screened-128x36'


class Screen128x40(Screen):
    device_type = 'screen-128x40'


class Screen128x48(Screen):
    device_type = 'screen-128x48'


class Screen128x52(Screen):
    device_type = 'screen-128x52'
