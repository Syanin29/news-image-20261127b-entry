# Entrypoint: draws the front page and writes /output/entry.png.
# Standard library + Pillow only; no network, no model calls, no
# randomness, no clock reads — two runs write identical bytes.
# Variant is picked by the MAKEFUN_VARIANT environment variable
# (default A-paper); the graded run uses the default.

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import render


def output_dir():
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    variant = os.environ.get("MAKEFUN_VARIANT", "A-paper")
    if variant not in render.VARIANTS:
        raise SystemExit("unknown variant: %s" % variant)
    image = render.render(variant)
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.png")
    image.save(path, format="PNG")
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    main()
