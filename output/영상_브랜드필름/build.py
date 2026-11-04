# ENOCH MUSIC ACADEMY — Brand Film (1080×1920, 약 20초, 무음)
# python3 build.py <원본 영상 폴더>   → film.mp4
# 원본 영상(IMG_27xx.mov)은 용량이 커서 저장소에 두지 않는다. 사진은 images/공간/.
import os, sys, subprocess, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '../..'))
SRC = sys.argv[1] if len(sys.argv) > 1 else '.'
TMP = os.path.join(HERE, '_tmp'); shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP)
FPS = 24
def vid(name):
    m = [f for f in os.listdir(SRC) if f.endswith(name + '.mov')]
    return os.path.join(SRC, m[0])

# (종류, 소스, 시작, 길이, 옵션) — 원본에 실제로 있는 장면만
CUTS = [
  ('photo', 'images/공간/피아노방_01.jpg', 'crop=1330:2364:0:212', 3.0),   # 오른쪽 달력·에어컨은 잘라냄
  ('photo', 'images/공간/복도_03.jpg',     'crop=1400:2489:0:87', 1.5),     # 오른쪽 CCTV는 잘라냄
  ('video', 'IMG_2727', 0.3, 1.5),   # 믹서·드럼 스틱
  ('video', 'IMG_2727', 1.9, 1.5),   # KORG 건반
  ('photo', 'images/공간/기타랙_01.jpg',   'crop=1449:2576:322:0', 2.0),
  ('video', 'IMG_2728', 0.0, 1.4),   # 드럼 정면
  ('video', 'IMG_2730', 0.0, 2.5),   # 앰프·헤링본 마루
  ('video', 'IMG_2730', 4.0, 2.9),   # 기타·식물 그림자·피아노
  ('end',   'IMG_2727', 3.3, 1.2, 2.3),  # 무대 와이드 → 문틀이 들어오기 전 정지
]
parts = []
for i, c in enumerate(CUTS):
    out = os.path.join(TMP, f'{i:02d}.mp4'); parts.append(out)
    if c[0] == 'photo':
        dur = c[3]; n = int(dur * FPS)
        vf = (f"{c[2]},scale=2160:3840,zoompan=z='1+0.045*on/{n}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'"
              f":d={n}:s=1080x1920:fps={FPS},setsar=1")
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', os.path.join(ROOT, c[1]), '-vf', vf, '-frames:v', str(n)]
    else:
        hold = c[4] if c[0] == 'end' else 0
        vf = f"trim=start={c[2]}:duration={c[3]},setpts=PTS-STARTPTS,fps={FPS},scale=1134:2016,crop=1080:1920,setsar=1"
        if hold: vf += f",tpad=stop_mode=clone:stop_duration={hold}"
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', vid(c[1]), '-an', '-vf', vf]
    subprocess.run(cmd + ['-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', out], check=True)
lst = os.path.join(TMP, 'list.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
base = os.path.join(TMP, 'base.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base], check=True)
TOTAL = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base]))

# 문구 (필요한 순간에만) — (파일, 시작, 끝)
TEXTS = [('t_enoch', 1.0, 2.8), ('t_space', 4.7, 7.3), ('t_detail', 7.7, 9.3), ('t_way', 13.7, 16.1), ('t_end', 17.0, TOTAL)]
subprocess.run(['node', os.path.join(HERE, 'texts.mjs')], check=True)
inputs = ['-i', base]; fc = "[0:v]eq=saturation=0.9:contrast=1.03:gamma=0.98,noise=alls=4:allf=t,format=yuv420p[v0];"
last = 'v0'
for k, (name, a, b) in enumerate(TEXTS):
    d = b - a
    inputs += ['-loop', '1', '-t', f'{d:.2f}', '-i', os.path.join(TMP, name + '.png')]
    fo = f",fade=out:st={d-0.6:.2f}:d=0.6:alpha=1" if b < TOTAL else ''
    fc += f"[{k+1}:v]format=rgba,fade=in:st=0:d=0.6:alpha=1{fo},setpts=PTS-STARTPTS+{a}/TB[t{k}];"
    fc += f"[{last}][t{k}]overlay=0:0:eof_action=pass[v{k+1}];"; last = f'v{k+1}'
fc += f"[{last}]fade=in:st=0:d=0.4,fade=out:st={TOTAL-0.6:.2f}:d=0.6[out]"
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', fc, '-map', '[out]', '-t', f'{TOTAL:.2f}',
                '-c:v', 'libx264', '-crf', '22', '-preset', 'slow', '-maxrate', '12M', '-bufsize', '24M', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                os.path.join(HERE, 'film.mp4')], check=True)
shutil.rmtree(TMP)
print('film.mp4', f'{TOTAL:.1f}s')
