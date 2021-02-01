import sys, json, random, numpy
import scipy.spatial.distance

def move(moves):
    record = {'moves': moves}
    print(json.dumps(record))
    sys.stdout.flush()

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
            dest = min(other_planets, key=lambda p: p['ship_count'])
            if planet['ship_count'] > dest['ship_count'] + 5:
                amount = planet['ship_count'] - dest['ship_count']
                moves.append({
                    'origin': planet['name'],
                    'destination': dest['name'],
                    'ship_count': planet['ship_count'] - amount +  5
                })
        move(moves)

# def OptimalDistance(my_planets, other_planets):
#     return Boolean  

# TODO: Euclidean distance


def ConstructCoordMatrix():

    CoordMatrix = [][]
    return CoordMatrix


# Matrix with coordinates to find nearest neighbour

def NearestNeighbour(CoordMatrix,sX,sY):
    # TODO
    return False
    


def GainedInDistance(sX,sY,oX,oY):
    return True
