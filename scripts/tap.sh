#!/bin/zsh
# tap.sh <x> <y>  — coords as seen in a 921x2000 rendering of the simulator screenshot
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN=/tmp/blast-simclick
[[ -x $BIN ]] || swiftc -O "$DIR/simclick.swift" -o $BIN || exit 1
osascript -e 'tell application "Simulator" to activate' >/dev/null 2>&1
GEO=$(osascript -e 'tell application "System Events" to tell process "Simulator" to get {position, size} of group 1 of window 1' | tr -d ' ')
python3 -c "
import sys, subprocess
gx, gy, gw, gh = [float(v) for v in '$GEO'.split(',')]
dx, dy = float(sys.argv[1]), float(sys.argv[2])
x = gx + (dx / 921.0) * gw
y = gy + (dy / 2000.0) * gh
subprocess.run(['$BIN', str(x), str(y)])
" "$1" "$2"
