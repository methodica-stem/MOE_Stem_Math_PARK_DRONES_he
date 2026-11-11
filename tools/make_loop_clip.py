"""Make a seamless, silent, web-ready loop from a generated clip (screen 10, "what the drone films").

  python tools/make_loop_clip.py <source.mp4> <out.mp4> [poster.jpg] [overlap_seconds=0.5]

What it does: decodes every frame, fades the last `overlap` seconds into the first ones (so the
end flows into the start with no jump), drops the audio, and re-encodes H.264 (libx264, CRF 22,
slow, yuv420p, high profile, BT.709 tagged, faststart). Uses the ffmpeg bundled with the
imageio-ffmpeg Python package (this machine has no system ffmpeg).
"""
import glob, os, shutil, subprocess, sys, tempfile
import numpy as np
from PIL import Image
import imageio_ffmpeg

src, dst = sys.argv[1], sys.argv[2]
poster = sys.argv[3] if len(sys.argv) > 3 else None
overlap = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
ff = imageio_ffmpeg.get_ffmpeg_exe()

tmp = tempfile.mkdtemp(prefix="loopclip_")
fin, fout = os.path.join(tmp, "in"), os.path.join(tmp, "out")
os.makedirs(fin); os.makedirs(fout)
subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-an", os.path.join(fin, "%04d.png")], check=True)
files = sorted(glob.glob(os.path.join(fin, "*.png")))
n = len(files)
fps = 24
k = max(2, int(round(overlap * fps)))
L = n - k
print(f"{n} frames, loop length {L} frames ({L / fps:.2f} s), crossfade {k} frames")

load = lambda i: np.asarray(Image.open(files[i]).convert("RGB")).astype(np.float32)
for i in range(L):
    if i < k:
        a = i / k                                   # 0 -> 1: from the tail of the clip into its head
        frame = load(L + i) * (1 - a) + load(i) * a
    else:
        frame = load(i)
    Image.fromarray(np.clip(frame + 0.5, 0, 255).astype(np.uint8)).save(os.path.join(fout, f"{i + 1:04d}.png"), compress_level=1)

subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y", "-framerate", str(fps), "-i", os.path.join(fout, "%04d.png"),
                "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
                "-c:v", "libx264", "-preset", "slow", "-crf", "22", "-profile:v", "high", "-pix_fmt", "yuv420p",
                "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
                "-an", "-movflags", "+faststart", dst], check=True)
if poster:
    Image.open(os.path.join(fout, "0001.png")).convert("RGB").save(poster, quality=88)
shutil.rmtree(tmp, ignore_errors=True)
print(dst, os.path.getsize(dst) // 1024, "KB")
