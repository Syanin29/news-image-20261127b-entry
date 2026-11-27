# Entrypoint: writes /output/entry.png (the front page for 27 Nov 2026).
# Standard library only in the graded run: the competition installs
# nothing, so Pillow may be absent. When Pillow is available the page
# is rendered fresh (deterministic); otherwise the pre-rendered image
# the repository holds is copied byte for byte. No network, no model
# calls, no randomness, no clock reads — two runs write identical bytes.
# Variant is picked by the MAKEFUN_VARIANT environment variable
# (default A-paper); the graded run uses the default.

import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import render
    _HAS_RENDER = True
except ImportError:
    render = None
    _HAS_RENDER = False


def output_dir():
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def _prerendered_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "out", "variants", "A-paper", "entry.png")


def main():
    variant = os.environ.get("MAKEFUN_VARIANT", "A-paper")
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.png")
    rendered = False
    if _HAS_RENDER:
        try:
            if variant not in render.VARIANTS:
                raise SystemExit("unknown variant: %s" % variant)
            image = render.render(variant)
            image.save(path, format="PNG")
            rendered = True
        except Exception:
            rendered = False
    if not rendered:
        shutil.copyfile(_prerendered_path(), path)
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    main()
