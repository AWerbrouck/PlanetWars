import sys, json, random,math

def move(moves):
    record = {'moves': moves}
    print(json.dumps(record))
    sys.stdout.flush()

for line in sys.stdin:
    state = json.loads(line)

    # find planet with most ships
    my_planets = [p for p in state['planets'] if p['owner'] == 1]
    other_planets = [p for p in state['planets'] if p['owner'] != 1]
    count = 0
    if not my_planets or not other_planets:
        move([])
    else:
        planet = max(my_planets, key=lambda p: p['ship_count'])
        dest = min(other_planets, abs(key=lambda p: p['x'] - planet['x']))
        if planet['ship_count'] > dest['ship_count'] + 5:
            amount = planet['ship_count'] - dest['ship_count']
            move([{
                'origin': planet['name'],
                'destination': dest['name'],
                'ship_count': planet['ship_count'] - amount +  5
            }])
        else:
            move([])


# def OptimalDistance(my_planets, other_planets):
#     return True
