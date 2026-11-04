# ENOCH MUSIC ACADEMY — Brand Film (1080×1920, 약 20초, 무음)
# 흔들림 없이: 원본 영상에서 가장 선명한 프레임을 골라 멈춘 화면으로 쓰고, 짧은 디졸브로 잇는다.
# python3 build.py <원본 영상 폴더>   → film.mp4   (Pillow·numpy 필요)
import os, sys, subprocess, shutil
import numpy as np
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '../..'))
SRC = sys.argv[1] if len(sys.argv) > 1 else '.'
TMP = os.path.join(HERE, '_tmp'); shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP)
FPS, XF = 24, 0.4
def vid(name):
    return os.path.join(SRC, [f for f in os.listdir(SRC) if f.endswith(name + '.mov')][0])

# (소스, 시점 또는 자르기, 길이) — 원본에 실제로 있는 장면만
SHOTS = [
  ('images/공간/피아노방_01.jpg', (0, 212, 1330, 2576), 3.0),  # MUSIC — 달력·에어컨 제외
  ('IMG_2733', 6.767, 1.8),   # 아치 복도
  ('IMG_2723', 0.75, 1.8),    # 스탠드 조명의 작은 방
  ('IMG_2727', 0.783, 2.2),   # CREATE — 믹서·드럼 스틱
  ('IMG_2727', 2.883, 1.8),   # KORG 건반
  ('IMG_2730', 0.917, 1.8),   # 앰프·헤링본 마루
  ('IMG_2730', 6.2, 2.4),     # PRACTICE — 식물 그림자·기타·피아노
  ('images/공간/기타랙_01.jpg', (322, 0, 1771, 2576), 1.8),
  ('IMG_2728', 0.0, 2.4),     # PERFORM — 무대 위 드럼
  ('IMG_2727', 4.067, 3.8),   # ENOCH — 무대 와이드 (마지막)
]

def grade(im):
    """조명이 다른 방들을 한 톤으로: 화이트밸런스 절반 보정 → 채도 낮춤 → 검정 살짝 들고 하이라이트 눌러 크림 톤."""
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    m = a.reshape(-1, 3).mean(0); g = m.mean()
    a = a * (1 + 0.5 * (g / m - 1))                       # 회색 기준 화이트밸런스 50%
    lum = (a * [0.299, 0.587, 0.114]).sum(-1, keepdims=True)
    a = lum + (a - lum) * 0.80                           # 채도 80%
    a = 0.035 + a * (0.95 - 0.035)                       # 블랙 리프트, 하이라이트 롤오프
    a = np.clip(a, 0, 1) ** 1.04
    a = 0.5 + (a - 0.5) * 1.08                           # 살짝 대비
    a = a + (1 - a) * np.array([0.012, 0.006, -0.010]) + a * np.array([0.010, 0.004, -0.012])  # 따뜻한 크림
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))

clips = []
for i, (src, at, dur) in enumerate(SHOTS):
    still = os.path.join(TMP, f's{i}.jpg')
    if src.startswith('IMG_'):
        raw = os.path.join(TMP, f'r{i}.jpg')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', vid(src), '-ss', str(at), '-frames:v', '1', '-q:v', '1', raw], check=True)
        im = Image.open(raw)
    else:
        im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, src))).crop(at)
    im = ImageOps.fit(im, (2160, 3840), Image.LANCZOS)
    grade(im).save(still, quality=95)
    n = int(dur * FPS); out = os.path.join(TMP, f'c{i}.mp4'); clips.append((out, dur))
    vf = f"scale=1080:1920,fps={FPS},setsar=1"   # 완전히 멈춘 화면
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', still, '-vf', vf, '-frames:v', str(n),
                    '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out], check=True)

# 디졸브로 잇기
inputs = sum([['-i', c] for c, _ in clips], [])
fc, last, t = '', '0:v', clips[0][1]
starts = [0.0]
for k in range(1, len(clips)):
    off = t - XF; starts.append(off)
    fc += f"[{last}][{k}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}[x{k}];"; last = f'x{k}'
    t = off + clips[k][1]
TOTAL = t
base = os.path.join(TMP, 'base.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', fc.rstrip(';'), '-map', f'[{last}]',
                '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', base], check=True)

# 문구 — 샷 시작 기준
S = starts
TEXTS = [('w_music', S[0] + 0.9, S[1]), ('w_create', S[3] + 0.4, S[4]), ('w_practice', S[6] + 0.4, S[7]), ('w_perform', S[8] + 0.4, S[9]), ('w_enoch', S[9] + 0.7, TOTAL)]
subprocess.run(['node', os.path.join(HERE, 'texts.mjs')], check=True)
inputs = ['-i', base]; fc = "[0:v]noise=alls=3:allf=t,format=yuv420p[v0];"; last = 'v0'
for k, (name, a, b) in enumerate(TEXTS):
    d = b - a
    inputs += ['-loop', '1', '-t', f'{d:.2f}', '-i', os.path.join(TMP, name + '.png')]
    fo = f",fade=out:st={d-0.6:.2f}:d=0.6:alpha=1" if b < TOTAL else ''
    fc += f"[{k+1}:v]format=rgba,fade=in:st=0:d=0.7:alpha=1{fo},setpts=PTS-STARTPTS+{a:.3f}/TB[t{k}];"
    fc += f"[{last}][t{k}]overlay=0:0:eof_action=pass[v{k+1}];"; last = f'v{k+1}'
fc += f"[{last}]fade=in:st=0:d=0.5,fade=out:st={TOTAL-0.7:.2f}:d=0.7[out]"
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', fc, '-map', '[out]', '-t', f'{TOTAL:.2f}',
                '-c:v', 'libx264', '-crf', '20', '-preset', 'slow', '-maxrate', '12M', '-bufsize', '24M',
                '-pix_fmt', 'yuv420p', '-movflags', '+faststart', os.path.join(HERE, 'film.mp4')], check=True)
for i in range(len(SHOTS)): shutil.copy(os.path.join(TMP, f's{i}.jpg'), os.path.join(HERE, '_preview', f'{i:02d}.jpg')) if os.path.isdir(os.path.join(HERE, '_preview')) else None
shutil.rmtree(TMP)
print('film.mp4', f'{TOTAL:.1f}s')
