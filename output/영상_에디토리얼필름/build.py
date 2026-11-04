# ENOCH MUSIC ACADEMY — Editorial Film (1080×1920, 약 22초, 무음, 92 BPM 컷)
# python3 build.py <원본 영상 폴더>  → film.mp4   (Pillow·numpy·node/playwright 필요)
# 흔들리는 핸드헬드 영상은 가장 선명한 한 프레임만 쓰고, 고정된 장면(베이스 레슨 손)만 실제 움직임으로 쓴다.
import os, sys, subprocess, shutil, glob
import numpy as np
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '../..'))
SRC = sys.argv[1] if len(sys.argv) > 1 else '.'
TMP = os.path.join(HERE, '_tmp'); shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP)
PRE = os.path.join(HERE, '_preview'); os.makedirs(PRE, exist_ok=True)
FPS, B = 24, 60 / 92            # 한 박
def vid(name): return os.path.join(SRC, [f for f in os.listdir(SRC) if f.endswith(name + '.mov')][0])
def src(p): return p if os.path.isabs(p) else os.path.join(ROOT, p)

# (이름, 소스, 시점|None, 자르기 box|None, 박 수, 움직임?)
SHOTS = [
  ('A 녹음 부스',     'images/공간/보컬부스_01.jpg', None, None, 2, False),
  ('B 건반',         'images/공간/피아노방_01.jpg', None, (60, 1225, 820, 2576), 2, False),
  ('O 보컬 손',       'eafeea67-image.png',         None, (150, 500, 794, 1645), 2, False),
  ('C 아치 복도',     'IMG_2733', 6.767, None, 2, False),
  ('L 강의실',        'IMG_2729', 0.42, None, 2, False),
  ('D 피아노 방',      'images/공간/피아노방_02.jpg', None, (180, 0, 1318, 2023), 2, False),
  ('E KORG',        'IMG_2727', 2.883, None, 1, False),
  ('G 휴게실',        'IMG_2723', 0.75, None, 2, False),
  ('F 기타 랙',       'images/공간/기타랙_01.jpg', None, (322, 0, 1771, 2576), 2, False),
  ('M 베이스 레슨',   '4172C8F8-5C89-48CF-B562-068D95E996D5', 2.0, (278, 990, 801, 1920), 3, True),
  ('I 상담실',        'IMG_2724', 3.08, None, 2, False),
  ('J 식물 그림자',   'IMG_2730', 6.2, None, 2, False),
  ('N 드럼 레슨 손',  'images/학생/드럼레슨_01.jpg', None, (480, 1290, 1180, 2534), 1, False),
  ('H 드럼 정면',     'IMG_2728', 0.0, None, 1, False),
  ('K 무대',         'IMG_2727', 4.067, None, 9, False),
]

def grade(im):
    # 기준: 원장님이 보내주신 피아노 방 사진 (따뜻한 호박빛, 깊은 검정, 자연스러운 채도)
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    m = a.reshape(-1, 3).mean(0); a = a * (1 + 0.35 * (m.mean() / m - 1))           # 형광등 색만 살짝 정리
    a = a * np.array([1.05, 1.0, 0.86])                                               # 호박빛
    lum = (a * [0.299, 0.587, 0.114]).sum(-1, keepdims=True)
    c = float((np.clip(a, 0, 1).max(-1) - np.clip(a, 0, 1).min(-1)).mean())
    a = lum + (a - lum) * min(1.05, 1.05 * (0.13 / max(c, 1e-6)) ** 0.5)             # 채도는 자연스럽게, 튀는 장면만 눌러 줌
    a = np.clip(a, 0, 1) ** 1.12; a = 0.5 + (a - 0.5) * 1.10                           # 깊은 검정, 단단한 대비
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))

def frame(name, s, at, box):
    if s.startswith('IMG_') or '4172C8F8' in s:
        raw = os.path.join(TMP, 'raw.png')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', vid(s), '-ss', str(at), '-frames:v', '1', raw], check=True)
        im = Image.open(raw)
    else:
        p = src(s) if not s.endswith('-image.png') else os.path.join(SRC, s)
        im = ImageOps.exif_transpose(Image.open(p))
    if box: im = im.crop(box)
    return ImageOps.fit(im, (1080, 1920), Image.LANCZOS)

clips, t, starts = [], 0.0, []
for i, (name, s, at, box, beats, moving) in enumerate(SHOTS):
    dur = beats * B; n = round(dur * FPS); starts.append(t); t += n / FPS
    out = os.path.join(TMP, f'c{i:02d}.mp4'); clips.append(out)
    if moving:   # 실제 움직임: 프레임마다 같은 색보정
        fd = os.path.join(TMP, f'm{i}'); os.makedirs(fd)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(at), '-i', vid(s), '-frames:v', str(n), '-vf',
                        f'fps={FPS},crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]},scale=1080:1920:flags=lanczos', os.path.join(fd, '%04d.png')], check=True)
        for f in sorted(glob.glob(os.path.join(fd, '*.png'))): grade(Image.open(f)).save(f)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', os.path.join(fd, '%04d.png'), '-frames:v', str(n),
                        '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out], check=True)
        shutil.copy(sorted(glob.glob(os.path.join(fd, '*.png')))[n // 2], os.path.join(PRE, f'{i:02d}.png'))
    else:
        st = os.path.join(TMP, f's{i}.png'); g = grade(frame(name, s, at, box)); g.save(st); g.save(os.path.join(PRE, f'{i:02d}.png'))
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', st, '-frames:v', str(n), '-vf', f'fps={FPS},setsar=1',
                        '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out], check=True)
TOTAL = t
lst = os.path.join(TMP, 'list.txt'); open(lst, 'w').write(''.join(f"file '{c}'\n" for c in clips))
base = os.path.join(TMP, 'base.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base], check=True)

# 타이포 상태 — 컷에 맞춰 툭 나타나고 툭 사라진다
S = starts
STATES = [('music', S[1], S[3]), ('space', S[3], S[5]), ('creation', S[5], S[6]), ('practice', S[9], S[10]),
          ('per1', S[12], S[13]), ('per2', S[13], S[14]), ('per3', S[14], S[14] + 2 * B), ('enoch', S[14] + 2 * B + 0.5, TOTAL)]
subprocess.run(['node', os.path.join(HERE, 'type.mjs')], check=True)
inputs = ['-i', base]; fc = '[0:v]noise=alls=3:allf=t,format=yuv420p[v0];'; last = 'v0'
for k, (name, a, b) in enumerate(STATES):
    inputs += ['-i', os.path.join(TMP, f'{name}.png')]
    fc += f"[{last}][{k+1}:v]overlay=0:0:enable='between(t,{a:.3f},{b - 0.001:.3f})'[v{k+1}];"; last = f'v{k+1}'
fc += f"[{last}]fade=out:st={TOTAL - 0.6:.2f}:d=0.6[out]"
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', fc, '-map', '[out]', '-t', f'{TOTAL:.3f}',
                '-c:v', 'libx264', '-crf', '20', '-preset', 'slow', '-maxrate', '12M', '-bufsize', '24M', '-pix_fmt', 'yuv420p',
                '-movflags', '+faststart', os.path.join(HERE, 'film.mp4')], check=True)
shutil.rmtree(TMP); print('film.mp4', f'{TOTAL:.2f}s', [round(x, 2) for x in S])
