#!/usr/bin/env bash
EGGDIR="window_detector.egg-info"
if [ -d "$EGGDIR" ]; then
    rm -rf ${EGGDIR}
fi
cd /app
poetry install
"$@"
