#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSET="$HERE/assets/skill-generalizer-hero.png"
BUILD="$HERE/assets/build"
OUT="$HERE/assets"
FONT_BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
mkdir -p "$BUILD"

scene() {
  local duration="$1" filter="$2" output="$3"
  ffmpeg -loglevel error -y -loop 1 -framerate 30 -t "$duration" -i "$ASSET" \
    -vf "$filter,format=yuv420p" -an -c:v libx264 -preset fast -crf 16 -r 30 "$output"
}

# 1. The retest exists before the lesson: push toward the teacher and locked capsule.
scene 2.70 \
  "zoompan=z='min(1.15+on*0.00055,1.20)':x='0':y='ih/2-(ih/zoom/2)':d=1:s=1600x900:fps=30,
   drawbox=x=64:y=742:w=605:h=112:color=0x10243B@0.90:t=fill,
   drawbox=x=64:y=742:w=12:h=112:color=0xFF6B57@1.0:t=fill,
   drawtext=fontfile='$FONT_BOLD':text='SEAL RETEST FIRST':fontsize=47:fontcolor=white:x=104:y=755,
   drawtext=fontfile='$FONT_REG':text='prepared before the patch':fontsize=27:fontcolor=0xCFE9FF:x=106:y=812" \
  "$BUILD/visual-1.mp4"

# 2. All students consult the same handbook: breathe around the center group.
scene 2.70 \
  "zoompan=z='1.17+0.018*sin(on*PI/81)':x='min(iw-iw/zoom,max(0,iw*0.56-iw/(2*zoom)))':y='ih*0.54-ih/(2*zoom)':d=1:s=1600x900:fps=30,
   drawbox=x=64:y=742:w=630:h=112:color=0x10243B@0.90:t=fill,
   drawbox=x=64:y=742:w=12:h=112:color=0x48B9EA@1.0:t=fill,
   drawtext=fontfile='$FONT_BOLD':text='ONE COMMON SKILL':fontsize=47:fontcolor=white:x=104:y=755,
   drawtext=fontfile='$FONT_REG':text='shared by every student':fontsize=27:fontcolor=0xCFE9FF:x=106:y=812" \
  "$BUILD/visual-2.mp4"

# 3. Partial success is rejected: push toward the three lights and return tray.
scene 2.70 \
  "zoompan=z='min(1.17+on*0.00070,1.23)':x='iw-iw/zoom':y='max(0,ih*0.45-ih/(2*zoom))':d=1:s=1600x900:fps=30,
   drawbox=x=64:y=742:w=790:h=112:color=0x10243B@0.90:t=fill,
   drawbox=x=64:y=742:w=12:h=112:color=0xFFD05A@1.0:t=fill,
   drawtext=fontfile='$FONT_BOLD':text='FAIL? REJECT THE PATCH':fontsize=45:fontcolor=white:x=104:y=755,
   drawtext=fontfile='$FONT_REG':text='partial success does not ship':fontsize=27:fontcolor=0xFFF0B8:x=106:y=812" \
  "$BUILD/visual-3.mp4"

# 4. Return to the whole system so the loop can restart cleanly.
scene 2.70 \
  "zoompan=z='max(1.0,1.055-on*0.00068)':x='iw/2-iw/(2*zoom)':y='ih/2-ih/(2*zoom)':d=1:s=1600x900:fps=30,
   drawbox=x=64:y=742:w=850:h=112:color=0x10243B@0.90:t=fill,
   drawbox=x=64:y=742:w=12:h=112:color=0x63C881@1.0:t=fill,
   drawtext=fontfile='$FONT_BOLD':text='OBSERVE  ·  PATCH  ·  RETEST':fontsize=38:fontcolor=white:x=104:y=758,
   drawtext=fontfile='$FONT_REG':text='keep only what every target proves':fontsize=27:fontcolor=0xD6F3DF:x=106:y=812" \
  "$BUILD/visual-4.mp4"

ffmpeg -loglevel error -y \
  -i "$BUILD/visual-1.mp4" -i "$BUILD/visual-2.mp4" \
  -i "$BUILD/visual-3.mp4" -i "$BUILD/visual-4.mp4" \
  -filter_complex "
    [0:v][1:v]xfade=transition=smoothleft:duration=0.25:offset=2.45[v1];
    [v1][2:v]xfade=transition=smoothleft:duration=0.25:offset=4.90[v2];
    [v2][3:v]xfade=transition=fade:duration=0.25:offset=7.35,
    format=yuv420p[v]" \
  -map "[v]" -an -c:v libx264 -preset medium -crf 17 -r 30 -movflags +faststart \
  "$OUT/teacher-student-loop.mp4"

ffmpeg -loglevel error -y -i "$OUT/teacher-student-loop.mp4" \
  -filter_complex "fps=10,scale=720:405:flags=lanczos,split[a][b];
    [a]palettegen=max_colors=96:stats_mode=diff[p];
    [b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" \
  -loop 0 "$OUT/teacher-student-loop.gif"

printf '%s\n' \
  "$OUT/skill-generalizer-hero.png" \
  "$OUT/teacher-student-loop.mp4" \
  "$OUT/teacher-student-loop.gif"
