#!/bin/bash


FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    git clone https://github.com/G2Wolverine3751/GalaxyUserbot.git galaxy_ub
    rm -rf userbot
    mv galaxy_ub/.git .
    mv galaxy_ub/userbot .
    mv galaxy_ub/requirements.txt .
    rm -rf galaxy_ub
    python ./.github/update.py
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    bash ./.github/bins.sh
fi

python -m userbot
