from flask import Flask, request

import game_sense

app = Flask('svz')


@app.route('/csgo_game_event', methods=['POST'])
def csgo():
    data = request.get_json()
    print(data)
    return 'ok'


@app.route('/dota2_game_event', methods=['POST'])
def dota2():
    data = request.get_json()
    print(data)
    return 'ok'


if __name__ == '__main__':
    props = game_sense.get_props()
    ip, port = props['address'].split(':')
    app.run(ip, int(port))
