from PIL import Image
import os, glob

TARGET_RATIO = 16/9

folders = [
    "coinwy/swapzone-batch/media",
    "Kanalcoin/swapzone-batch/media",
    "DeFiLiban/swapzone-batch/media",
]

cropped = 0
skipped = 0

for folder in folders:
    for p in sorted(glob.glob(folder + "/*.png")):
        try:
            img = Image.open(p)
            w, h = img.size
            ratio = w / h
            
            if abs(ratio - TARGET_RATIO) / TARGET_RATIO < 0.05:
                skipped += 1
                continue
            
            target_h = int(w / TARGET_RATIO)
            if target_h >= h:
                skipped += 1
                continue
            
            cropped_img = img.crop((0, 0, w, target_h))
            cropped_img.save(p, "PNG", optimize=True)
            print(f"CROP {os.path.basename(p)}: {w}x{h} -> {w}x{target_h}")
            cropped += 1
        except Exception as e:
            print(f"ERROR {p}: {e}")

print(f"Done: {cropped} cropped, {skipped} already 16:9")
