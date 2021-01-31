import sys, json, random

def move(moves):
    record = {'moves': moves}
    print(json.dumps(record))
    sys.stdout.flush()

for line in sys.stdin:
    state = json.loads(line)

    # find planet with most ships
    my_planets = [p for p in state['planets'] if p['owner'] == 1]
    other_planets = [p for p in state['planets'] if p['owner'] != 1]
    if not my_planets or not other_planets:
        move([])
    else:
        for planet in my_planets:
            dest = min(other_planets, key=lambda p: p['ship_count'])
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
