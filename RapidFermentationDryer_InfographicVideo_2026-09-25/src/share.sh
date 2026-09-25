#!/bin/bash
# 共有用の 720p 版（30MB 未満）を 2パスで作る。 share.sh 入力.mp4 出力.mp4
set -e
IN="$1"; OUT="$2"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
VB=$(python3 -c "print(int((28.0*8*1024*1024/$DUR - 128000)/1000))")
cd "$(mktemp -d)"
ffmpeg -v error -y -i "$IN" -vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -b:v ${VB}k -pass 1 -g 60 -an -f mp4 /dev/null
ffmpeg -v error -y -i "$IN" -vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -b:v ${VB}k -pass 2 -g 60 -c:a aac -b:a 128k -movflags +faststart "$OUT"
echo "$OUT ${VB}k $(du -m "$OUT" | cut -f1)MB"
