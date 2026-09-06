"""Crop shield logo, emit favicons, compress work screenshots."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BRAND = ASSETS / "brand"
WORK = ASSETS / "work"
BRAND.mkdir(parents=True, exist_ok=True)


def bbox_nonblack(im: Image.Image, threshold: int = 18) -> tuple[int, int, int, int]:
    rgba = im.convert("RGBA")
    pixels = rgba.load()
    w, h = rgba.size
    min_x, min_y, max_x, max_y = w, h, 0, 0
    found = False
    step = 2
    for y in range(0, h, step):
        for x in range(0, w, step):
            r, g, b, a = pixels[x, y]
            if a < 8:
                continue
            if r > threshold or g > threshold or b > threshold:
                found = True
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
    if not found:
        return (0, 0, w, h)
    pad = 12
    return (
        max(0, min_x - pad),
        max(0, min_y - pad),
        min(w, max_x + pad + 1),
        min(h, max_y + pad + 1),
    )


def crop_logo():
    src = ROOT / "Shield-logo.png"
    im = Image.open(src)
    box = bbox_nonblack(im)
    cropped = im.crop(box)
    out = BRAND / "shield-mark.png"
    cropped.save(out, "PNG", optimize=True)
    print(f"cropped logo {im.size} -> {cropped.size} {out}")

    # Favicon sizes from cropped mark
    for size, name in ((32, "favicon-32.png"), (48, "favicon-48.png"), (180, "apple-touch-icon.png")):
        canvas = Image.new("RGBA", (size, size), (8, 9, 11, 255))
        mark = cropped.convert("RGBA")
        mark.thumbnail((size, size), Image.Resampling.LANCZOS)
        x = (size - mark.width) // 2
        y = (size - mark.height) // 2
        canvas.paste(mark, (x, y), mark)
        dest = BRAND / name
        canvas.save(dest, "PNG", optimize=True)
        print(f"wrote {dest}")

    # ICO
    ico = Image.open(BRAND / "favicon-48.png").convert("RGBA")
    ico.save(ROOT / "favicon.ico", format="ICO", sizes=[(32, 32), (48, 48)])
    print("wrote favicon.ico")


def compress_shots():
    if not WORK.exists():
        print("no work shots yet")
        return
    for png in WORK.glob("*.png"):
        im = Image.open(png).convert("RGB")
        jpg = png.with_suffix(".jpg")
        im.save(jpg, "JPEG", quality=84, optimize=True, progressive=True)
        print(f"jpg {jpg.name} {jpg.stat().st_size}")


if __name__ == "__main__":
    crop_logo()
    compress_shots()
