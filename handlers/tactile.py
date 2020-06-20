# !/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json

from define import devices
from handlers import base
from handlers.base import Data, Handlers, Mode


class Tactile(Handlers):
    def __init__(self, pattern, rate: base.Rate = None):
        """
        :param pattern: StaticPattern | RangePattern
        :param rate:
        """
        super().__init__(devices.Tactile.device_type,
                         devices.Tactile.zone.One, Mode.Vibrate)
        self.pattern = pattern
        self.rate = rate


class PredefinedPattern(Data):
    def __init__(self, tp, delay_ms=None):
        """
        :param tp:PredefinedPatternType
        :param delay_ms:
        """
        self.type = tp
        self.delay_ms = delay_ms


class CustomPattern(Data):
    def __init__(self, length_ms, delay_ms=None):
        self.type = 'custom'
        self.length_ms = length_ms
        self.delay_ms = delay_ms


class StaticPattern(Data):
    def __init__(self, *patterns):
        """
        :param patterns:[ PredefinedPattern | CustomPattern ]
        """
        self.patterns = patterns

    def data(self):
        return [i.data() for i in self.patterns]


class RangePattern(Data):
    def __init__(self, low, high, pattern=None):
        """
        :param low: event value, low end of range
        :param high: event value, high end of range
        :param pattern: StaticPattern | RangePattern
        """
        self.low = low
        self.high = high
        self.pattern = pattern
        if pattern is None:
            self.pattern = []


class PredefinedPatternType:
    TiPredefinedStrongClick100 = 'ti_predefined_strongclick_100'
    TiPredefinedStrongClick60 = 'ti_predefined_strongclick_60'
    TiPredefinedStrongClick30 = 'ti_predefined_strongclick_30'
    TiPredefinedSharpClick100 = 'ti_predefined_sharpclick_100'
    TiPredefinedSharpClick60 = 'ti_predefined_sharpclick_60'
    TiPredefinedSharpClick30 = 'ti_predefined_sharpclick_30'
    TiPredefinedSoftBump100 = 'ti_predefined_softbump_100'
    TiPredefinedSoftBump60 = 'ti_predefined_softbump_60'
    TiPredefinedSoftBump30 = 'ti_predefined_softbump_30'
    TiPredefinedDoubleClick100 = 'ti_predefined_doubleclick_100'
    TiPredefinedDoubleClick60 = 'ti_predefined_doubleclick_60'
    TiPredefinedTripleClick100 = 'ti_predefined_tripleclick_100'
    TiPredefinedSoftFuzz60 = 'ti_predefined_softfuzz_60'
    TiPredefinedStrongBuzz100 = 'ti_predefined_strongbuzz_100'
    TiPredefinedBuzzAlert750Ms = 'ti_predefined_buzzalert750ms'
    TiPredefinedBuzzAlert1000Ms = 'ti_predefined_buzzalert1000ms'
    TiPredefinedStrongClick1100 = 'ti_predefined_strongclick1_100'
    TiPredefinedStrongClick280 = 'ti_predefined_strongclick2_80'
    TiPredefinedStrongClick360 = 'ti_predefined_strongclick3_60'
    TiPredefinedStrongClick430 = 'ti_predefined_strongclick4_30'
    TiPredefinedMediumClick1100 = 'ti_predefined_mediumclick1_100'
    TiPredefinedMediumClick280 = 'ti_predefined_mediumclick2_80'
    TiPredefinedMediumClick360 = 'ti_predefined_mediumclick3_60'
    TiPredefinedSharpTick1100 = 'ti_predefined_sharptick1_100'
    TiPredefinedSharpTick280 = 'ti_predefined_sharptick2_80'
    TiPredefinedSharpTick360 = 'ti_predefined_sharptick3_60'
    TiPredefinedShortDoubleClickStrong1100 = 'ti_predefined_shortdoubleclickstrong1_100'
    TiPredefinedShortDoubleClickStrong280 = 'ti_predefined_shortdoubleclickstrong2_80'
    TiPredefinedShortDoubleClickStrong360 = 'ti_predefined_shortdoubleclickstrong3_60'
    TiPredefinedShortDoubleClickStrong430 = 'ti_predefined_shortdoubleclickstrong4_30'
    TiPredefinedShortDoubleClickMedium1100 = 'ti_predefined_shortdoubleclickmedium1_100'
    TiPredefinedShortDoubleClickMedium280 = 'ti_predefined_shortdoubleclickmedium2_80'
    TiPredefinedShortDoubleClickMedium360 = 'ti_predefined_shortdoubleclickmedium3_60'
    TiPredefinedShortDoubleSharpTick1100 = 'ti_predefined_shortdoublesharptick1_100'
    TiPredefinedShortDoubleSharpTick280 = 'ti_predefined_shortdoublesharptick2_80'
    TiPredefinedShortDoubleSharpTick360 = 'ti_predefined_shortdoublesharptick3_60'
    TiPredefinedLongDoubleSharpClickStrong1100 = 'ti_predefined_longdoublesharpclickstrong1_100'
    TiPredefinedLongDoubleSharpClickStrong280 = 'ti_predefined_longdoublesharpclickstrong2_80'
    TiPredefinedLongDoubleSharpClickStrong360 = 'ti_predefined_longdoublesharpclickstrong3_60'
    TiPredefinedLongDoubleSharpClickStrong430 = 'ti_predefined_longdoublesharpclickstrong4_30'
    TiPredefinedLongDoubleSharpClickMedium1100 = 'ti_predefined_longdoublesharpclickmedium1_100'
    TiPredefinedLongDoubleSharpClickMedium280 = 'ti_predefined_longdoublesharpclickmedium2_80'
    TiPredefinedLongDoubleSharpClickMedium360 = 'ti_predefined_longdoublesharpclickmedium3_60'
    TiPredefinedLongDoubleSharpTick1100 = 'ti_predefined_longdoublesharptick1_100'
    TiPredefinedLongDoubleSharpTick280 = 'ti_predefined_longdoublesharptick2_80'
    TiPredefinedLongDoubleSharpTick360 = 'ti_predefined_longdoublesharptick3_60'
    TiPredefinedBuzz1100 = 'ti_predefined_buzz1_100'
    TiPredefinedBuzz280 = 'ti_predefined_buzz2_80'
    TiPredefinedBuzz360 = 'ti_predefined_buzz3_60'
    TiPredefinedBuzz440 = 'ti_predefined_buzz4_40'
    TiPredefinedBuzz520 = 'ti_predefined_buzz5_20'
    TiPredefinedPulsingStrong1100 = 'ti_predefined_pulsingstrong1_100'
    TiPredefinedPulsingStrong260 = 'ti_predefined_pulsingstrong2_60'
    TiPredefinedPulsingMedium1100 = 'ti_predefined_pulsingmedium1_100'
    TiPredefinedPulsingMedium260 = 'ti_predefined_pulsingmedium2_60'
    TiPredefinedPulsingSharp1100 = 'ti_predefined_pulsingsharp1_100'
    TiPredefinedPulsingSharp260 = 'ti_predefined_pulsingsharp2_60'
    TiPredefinedTransitionClick1100 = 'ti_predefined_transitionclick1_100'
    TiPredefinedTransitionClick280 = 'ti_predefined_transitionclick2_80'
    TiPredefinedTransitionClick360 = 'ti_predefined_transitionclick3_60'
    TiPredefinedTransitionClick440 = 'ti_predefined_transitionclick4_40'
    TiPredefinedTransitionClick520 = 'ti_predefined_transitionclick5_20'
    TiPredefinedTransitionClick610 = 'ti_predefined_transitionclick6_10'
    TiPredefinedTransitionHum1100 = 'ti_predefined_transitionhum1_100'
    TiPredefinedTransitionHum280 = 'ti_predefined_transitionhum2_80'
    TiPredefinedTransitionHum360 = 'ti_predefined_transitionhum3_60'
    TiPredefinedTransitionHum440 = 'ti_predefined_transitionhum4_40'
    TiPredefinedTransitionHum520 = 'ti_predefined_transitionhum5_20'
    TiPredefinedTransitionHum610 = 'ti_predefined_transitionhum6_10'
    TiPredefinedTransitionRampDownLongSmooth1100To0 = 'ti_predefined_transitionrampdownlongsmooth1_100to0'
    TiPredefinedTransitionRampDownLongSmooth2100To0 = 'ti_predefined_transitionrampdownlongsmooth2_100to0'
    TiPredefinedTransitionRampDownMediumSmooth1100To0 = 'ti_predefined_transitionrampdownmediumsmooth1_100to0'
    TiPredefinedTransitionRampDownMediumSmooth2100To0 = 'ti_predefined_transitionrampdownmediumsmooth2_100to0'
    TiPredefinedTransitionRampDownShortSmooth1100To0 = 'ti_predefined_transitionrampdownshortsmooth1_100to0'
    TiPredefinedTransitionRampDownShortSmooth2100To0 = 'ti_predefined_transitionrampdownshortsmooth2_100to0'
    TiPredefinedTransitionRampDownLongSharp1100To0 = 'ti_predefined_transitionrampdownlongsharp1_100to0'
    TiPredefinedTransitionRampDownLongSharp2100To0 = 'ti_predefined_transitionrampdownlongsharp2_100to0'
    TiPredefinedTransitionRampDownMediumSharp1100To0 = 'ti_predefined_transitionrampdownmediumsharp1_100to0'
    TiPredefinedTransitionRampDownMediumSharp2100To0 = 'ti_predefined_transitionrampdownmediumsharp2_100to0'
    TiPredefinedTransitionRampDownShortSharp1100To0 = 'ti_predefined_transitionrampdownshortsharp1_100to0'
    TiPredefinedTransitionRampDownShortSharp2100To0 = 'ti_predefined_transitionrampdownshortsharp2_100to0'
    TiPredefinedTransitionRampUpLongSmooth10To100 = 'ti_predefined_transitionrampuplongsmooth1_0to100'
    TiPredefinedTransitionRampUpLongSmooth20To100 = 'ti_predefined_transitionrampuplongsmooth2_0to100'
    TiPredefinedTransitionRampUpMediumSmooth10To100 = 'ti_predefined_transitionrampupmediumsmooth1_0to100'
    TiPredefinedTransitionRampUpMediumSmooth20To100 = 'ti_predefined_transitionrampupmediumsmooth2_0to100'
    TiPredefinedTransitionRampUpShortSmooth10To100 = 'ti_predefined_transitionrampupshortsmooth1_0to100'
    TiPredefinedTransitionRampUpShortSmooth20To100 = 'ti_predefined_transitionrampupshortsmooth2_0to100'
    TiPredefinedTransitionRampUpLongSharp10To100 = 'ti_predefined_transitionrampuplongsharp1_0to100'
    TiPredefinedTransitionRampUpLongSharp20To100 = 'ti_predefined_transitionrampuplongsharp2_0to100'
    TiPredefinedTransitionRampUpMediumSharp10To100 = 'ti_predefined_transitionrampupmediumsharp1_0to100'
    TiPredefinedTransitionRampUpMediumSharp20To100 = 'ti_predefined_transitionrampupmediumsharp2_0to100'
    TiPredefinedTransitionRampUpShortSharp10To100 = 'ti_predefined_transitionrampupshortsharp1_0to100'
    TiPredefinedTransitionRampUpShortSharp20To100 = 'ti_predefined_transitionrampupshortsharp2_0to100'
    TiPredefinedTransitionRampDownLongSmooth150To0 = 'ti_predefined_transitionrampdownlongsmooth1_50to0'
    TiPredefinedTransitionRampDownLongSmooth250To0 = 'ti_predefined_transitionrampdownlongsmooth2_50to0'
    TiPredefinedTransitionRampDownMediumSmooth150To0 = 'ti_predefined_transitionrampdownmediumsmooth1_50to0'
    TiPredefinedTransitionRampDownMediumSmooth250To0 = 'ti_predefined_transitionrampdownmediumsmooth2_50to0'
    TiPredefinedTransitionRampDownShortSmooth150To0 = 'ti_predefined_transitionrampdownshortsmooth1_50to0'
    TiPredefinedTransitionRampDownShortSmooth250To0 = 'ti_predefined_transitionrampdownshortsmooth2_50to0'
    TiPredefinedTransitionRampDownLongSharp150To0 = 'ti_predefined_transitionrampdownlongsharp1_50to0'
    TiPredefinedTransitionRampDownLongSharp250To0 = 'ti_predefined_transitionrampdownlongsharp2_50to0'
    TiPredefinedTransitionRampDownMediumSharp150To0 = 'ti_predefined_transitionrampdownmediumsharp1_50to0'
    TiPredefinedTransitionRampDownMediumSharp250To0 = 'ti_predefined_transitionrampdownmediumsharp2_50to0'
    TiPredefinedTransitionRampDownShortSharp150To0 = 'ti_predefined_transitionrampdownshortsharp1_50to0'
    TiPredefinedTransitionRampDownShortSharp250To0 = 'ti_predefined_transitionrampdownshortsharp2_50to0'
    TiPredefinedTransitionRampUpLongSmooth10To50 = 'ti_predefined_transitionrampuplongsmooth1_0to50'
    TiPredefinedTransitionRampUpLongSmooth20To50 = 'ti_predefined_transitionrampuplongsmooth2_0to50'
    TiPredefinedTransitionRampUpMediumSmooth10To50 = 'ti_predefined_transitionrampupmediumsmooth1_0to50'
    TiPredefinedTransitionRampUpMediumSmooth20To50 = 'ti_predefined_transitionrampupmediumsmooth2_0to50'
    TiPredefinedTransitionRampUpShortSmooth10To50 = 'ti_predefined_transitionrampupshortsmooth1_0to50'
    TiPredefinedTransitionRampUpShortSmooth20To50 = 'ti_predefined_transitionrampupshortsmooth2_0to50'
    TiPredefinedTransitionRampUpLongSharp10To50 = 'ti_predefined_transitionrampuplongsharp1_0to50'
    TiPredefinedTransitionRampUpLongSharp20To50 = 'ti_predefined_transitionrampuplongsharp2_0to50'
    TiPredefinedTransitionRampUpMediumSharp10To50 = 'ti_predefined_transitionrampupmediumsharp1_0to50'
    TiPredefinedTransitionRampUpMediumSharp20To50 = 'ti_predefined_transitionrampupmediumsharp2_0to50'
    TiPredefinedTransitionRampUpShortSharp10To50 = 'ti_predefined_transitionrampupshortsharp1_0to50'
    TiPredefinedTransitionRampUpShortSharp20To50 = 'ti_predefined_transitionrampupshortsharp2_0to50'
    TiPredefinedLongBuzzForProgrammaticStopping100 = 'ti_predefined_longbuzzforprogrammaticstopping_100'
    TiPredefinedSmoothHum1NoKickOrBrakePulse50 = 'ti_predefined_smoothhum1nokickorbrakepulse_50'
    TiPredefinedSmoothHum2NoKickOrBrakePulse40 = 'ti_predefined_smoothhum2nokickorbrakepulse_40'
    TiPredefinedSmoothHum3NoKickOrBrakePulse30 = 'ti_predefined_smoothhum3nokickorbrakepulse_30'
    TiPredefinedSmoothHum4NoKickOrBrakePulse20 = 'ti_predefined_smoothhum4nokickorbrakepulse_20'
    TiPredefinedSmoothHum5NoKickOrBrakePulse10 = 'ti_predefined_smoothhum5nokickorbrakepulse_10'


def test():
    print(json.dumps(
        Tactile(
            StaticPattern(
                RangePattern(61, 100),
                RangePattern(26, 60, StaticPattern(PredefinedPattern(
                    PredefinedPatternType.TiPredefinedSharpClick60))),
                RangePattern(1, 25, StaticPattern(
                    CustomPattern(100, 150),
                    CustomPattern(250)
                ))
            ),
        ).data()))
    print(json.dumps(
        Tactile(
            StaticPattern(),
        ).data()))


if __name__ == '__main__':
    test()
