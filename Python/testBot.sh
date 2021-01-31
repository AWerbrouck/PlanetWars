#!/usr/bin/env bash
### SWAMP ###

keyOne="$1"
keyTwo="$2"


exec python3 runner.py -p 7000 --host planetwars.zeus.gent -n simple -i $keyOne python3 simple.py & exec python3 runner.py -p 7000 --host planetwars.zeus.gent -n sv01 -i $keyTwo  python3 genTwo.py 



