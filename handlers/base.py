class Data:
    def data(self):
        m = {}
        for k, v in self.__dict__.items():
            k = k.replace('_', '-')
            if isinstance(v, Data):
                m[k] = v.data()
            elif v is not None:
                m[k] = v
        return m


class Handlers(Data):
    def __init__(self, device_type, zone, mode):
        """
        :param device_type: define.Device.device_type
        :param zone: define.Device.zone
        :param mode: Mode
        """
        self.device_type = device_type
        self.zone = zone
        self.mode = mode


class RangeFrequency(Data):
    def __init__(self, low, high, frequency):
        """
        :param low: event value, low end of range
        :param high: event value, high end of range
        :param frequency:  value | RangeFrequency
        """
        self.low = low
        self.high = high
        self.frequency = frequency


class RangeRepeatLimit(Data):
    def __init__(self, low, high, repeat_limit):
        """
        :param low: event value, low end of range
        :param high: event value, high end of range
        :param repeat_limit: value
        """
        self.low = low
        self.high = high
        self.repeat_limit = repeat_limit


class Rate(Data):
    def __init__(self, frequency, repeat_limit=None):
        """
        :param frequency: value | RangeFrequency
        :param repeat_limit: value | RangeRepeatLimit
        """
        self.frequency = frequency
        self.repeat_limit = repeat_limit


class Mode:
    # color
    Count = 'count'
    Percent = 'percent'
    Color = 'color'
    # tactile
    Vibrate = 'vibrate'
    # screen
    Screen = 'screen'
    # full keyboard lighting
    Bitmap = 'bitmap'
    PartialBitmap = 'partial-bitmap'
