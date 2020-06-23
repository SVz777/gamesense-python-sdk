import json
import os

import requests


def get_props():
    if os.name == 'nt':
        props_path = os.path.expandvars(
            r'%PROGRAMDATA%/SteelSeries/SteelSeries Engine 3/coreProps.json')
    elif os.name == 'mac':
        props_path = os.path.expandvars(
            r'/Library/Application Support/SteelSeries Engine 3/coreProps.json')
    else:
        raise Exception('not support')

    with open(props_path, 'r') as f:
        content = f.read()
        return json.loads((content))


class GameSense:
    __PATH_GAME_METADATA = '/game_metadata'
    __PATH_REMOVE_GAME = '/remove_game'
    __PATH_GAME_HEARTBEAT = "/game_heartbeat"
    __PATH_REGISTER_GAME_EVENT = '/register_game_event'
    __PATH_REMOVE_GAME_EVENT = '/remove_game_event'
    __PATH_MULTIPLE_GAME_EVENTS = '/multiple_game_events'
    __PATH_GAME_EVENT = '/game_event'
    __PATH_BIND_GAME_EVENT = '/bind_game_event'

    def __init__(self, game):
        self.game = game
        self.__ss = requests.session()
        self.__url = f"http://{get_props()['address']}"

    def __post(self, path, data):
        return requests.post(f'{self.__url}{path}', json=data)

    def register_game(
            self,
            game_display_name='',
            icon_color_id=1,
            developer='',
            deinitialize_timer_length_ms=15000):
        ret = self.__post(self.__PATH_GAME_METADATA,
                          {
                              'game': self.game,
                              'developer': developer,
                              'game_display_name': game_display_name,
                              'icon_color_id': icon_color_id,
                              'deinitialize_timer_length_ms': deinitialize_timer_length_ms
                          })
        return ret.json()

    def remove_game(self):
        ret = self.__post(self.__PATH_REMOVE_GAME,
                          {
                              'game': self.game,
                          })
        return ret.json()

    def game_heartbeat(self):
        ret = self.__post(self.__PATH_REMOVE_GAME,
                          {
                              'game': self.game,
                          })

        return ret.json()

    def register_game_event(
            self,
            event,
            min_value=0,
            max_value=100,
            icon_id=0,
            value_optional=False,
            handlers=None):
        if handlers is None:
            handlers = []
        ret = self.__post(self.__PATH_REGISTER_GAME_EVENT,
                          {
                              'game': self.game,
                              'event': event,
                              'min_value': min_value,
                              'max_value': max_value,
                              'icon_id': icon_id,
                              'value_optional': value_optional,
                              'handlers': [i.data() for i in handlers]
                          })
        return ret.json()

    def bind_game_event(
            self,
            event,
            min_value=0,
            max_value=100,
            icon_id=0,
            value_optional=False,
            handlers=None):
        if handlers is None:
            handlers = []
        ret = self.__post(self.__PATH_BIND_GAME_EVENT,
                          {
                              'game': self.game,
                              'event': event,
                              'min_value': min_value,
                              'max_value': max_value,
                              'icon_id': icon_id,
                              'value_optional': value_optional,
                              'handlers': [i.data() for i in handlers]
                          })
        return ret.json()

    def remove_game_event(self, event):
        ret = self.__post(self.__PATH_REMOVE_GAME_EVENT,
                          {
                              'game': self.game,
                              'event': event,
                          })
        return ret.json()

    def send_game_event(self, event, data):
        ret = self.__post(self.__PATH_GAME_EVENT,
                          {
                              'game': self.game,
                              'event': event,
                              'data': data,
                          })
        return ret.json()
