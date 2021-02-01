#!/usr/bin/env bash
### SWAMP ###

keyOne="$1"
keyTwo="$2"

nameOne="$3"
scriptOne="$4"
nameTwo="$5"
scriptTwo="$6"
if [ - z nameOne ]; then
    nameOne="simple"
fi
if [ - z nameTwo ]; then
    nameTwo="Swamp"
fi
if [ - z scriptOne ]; then
    scriptOne="simple.py"
fi
if [ - z scriptTwo ]; then
    scriptTwo="genTwo.py"
fi

exec python3 runner.py -p 7000 --host planetwars.zeus.gent -n $nameOne -i $keyOne python3 $scriptOne & exec python3 runner.py -p 7000 --host planetwars.zeus.gent -n $nameTwo -i $keyTwo  python3 $scriptTwo 



