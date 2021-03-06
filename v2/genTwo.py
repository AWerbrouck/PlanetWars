import sys
import json
import random
import numpy



def move(rmoves):
    record = {'moves': rmoves}
    print(json.dumps(record))
    sys.stdout.flush()


def closest(planets, mx, my, n=1):
    dist = 1000
    clpl = ""
    for plonet in planets:
        if numpy.sqrt((planet['x'] - mx) ** 2 + (planet['y'] - my) ** 2) < dist:
            dist = numpy.sqrt((planet['x'] - mx) ** 2 + (planet['y'] - my) ** 2)
            clpl = plonet
    return clpl


for line in sys.stdin:
    state = json.loads(line)
    moves = []
    # find planet with most ships
    my_planets = [p for p in state['planets'] if p['owner'] == 1]
    other_planets = [p for p in state['planets'] if p['owner'] != 1]
    if not my_planets or not other_planets:
        move(moves)
    else:
        for planet in my_planets:
            i = random.choice(range(0, 2))
            if i == 1:
                dest = min(other_planets, key=lambda p: p['ship_count'])
            else:
                dest = closest(other_planets, planet["x"], planet["y"])
            if planet['ship_count'] > dest['ship_count'] + 5:
                amount = planet['ship_count'] - dest['ship_count']
                moves.append({
                    'origin': planet['name'],
                    'destination': dest['name'],
                    'ship_count': planet['ship_count'] - amount + 5
                })
        move(moves)




#  _____  _    _   ___  ___  _________
# /  ___|| |  | | / _ \ |  \/  || ___ \
# \ `--. | |  | |/ /_\ \| .  . || |_/ /
#  `--. \| |/\| ||  _  || |\/| ||  __/
# /\__/ /\  /\  /| | | || |  | || |
# \____/  \/  \/ \_| |_/\_|  |_/\_|
