#!/bin/bash
# 場面を3本並列で撮って、つなぐ。  ./render_lang.sh ja
set -e
L=$1
cd "$(dirname "$0")"
rm -rf build/seg_$L; mkdir -p build/seg_$L
for k in 0 1 2; do node render.js $L video $k 3 > build/render_${L}_$k.log 2>&1 & done
wait
ls build/seg_$L/*.mp4 | sort | sed "s#^build/seg_$L/#file '#; s#\$#'#" > build/seg_$L/list.txt
ffmpeg -v error -y -f concat -safe 0 -i build/seg_$L/list.txt -c copy build/silent_$L.mp4
echo "done $L $(ffprobe -v error -show_entries format=duration -of csv=p=0 build/silent_$L.mp4)"
