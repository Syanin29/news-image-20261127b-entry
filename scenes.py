# Drawn scenes: small vector illustrations, one per story card.
# Every scene is drawn from primitives (no photos, no external art),
# on a coloured sky panel with a ground band, a highlight and depth.
# Palette keys: sky, sky2, ground, ink, accent, paper, white.

from PIL import ImageDraw


def _sky(d, x, y, w, h, p):
    d.rectangle([x, y, x + w, y + h], fill=p["sky"])
    d.rectangle([x, y, x + w, y + int(h * 0.45)], fill=p["sky2"])
    d.rectangle([x, y + int(h * 0.78), x + w, y + h], fill=p["ground"])


def _sun(d, x, y, w, h, p):
    cx, cy, r = x + int(w * 0.78), y + int(h * 0.22), max(6, w // 12)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=p["sun"])
    d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2],
              fill=p["sun2"])


def _cloud(d, x, y, w, p):
    d.ellipse([x, y, x + w, y + int(w * 0.55)], fill=p["white"])
    d.ellipse([x + int(w * 0.2), y - int(w * 0.2), x + int(w * 0.8),
               y + int(w * 0.4)], fill=p["white"])


def _waves(d, x, y, w, p):
    for i, yy in enumerate((0, 8, 16)):
        c = p["wave"] if i % 2 == 0 else p["wave2"]
        d.arc([x, y + yy, x + w, y + yy + 14], 0, 180, fill=c, width=2)


def _burst(d, cx, cy, r, p):
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=p["accent"])
    d.ellipse([cx - r // 3, cy - r // 3, cx + r // 3, cy + r // 3],
              fill=p["sun"])


def _smoke(d, x, y, w, p):
    for i, r in enumerate((7, 10, 13)):
        d.ellipse([x + i * 8, y - i * 6, x + i * 8 + r * 2,
                   y - i * 6 + r * 2], fill=p["smoke"])


def scene_drone(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _sun(d, x, y, w, h, p)
    cx, cy = x + w // 2, y + int(h * 0.45)
    d.line([cx - 26, cy - 8, cx + 26, cy - 8], fill=p["ink"], width=3)
    d.ellipse([cx - 12, cy - 8, cx + 12, cy + 8], fill=p["ink"])
    d.ellipse([cx - 4, cy - 3, cx + 4, cy + 3], fill=p["accent"])
    for sx in (-30, 30):
        d.line([cx + sx - 9, cy - 14, cx + sx + 9, cy - 14],
               fill=p["ink"], width=3)
        d.ellipse([cx + sx - 4, cy - 15, cx + sx + 4, cy - 9], fill=p["ink"])
    d.line([cx, cy + 8, cx, cy + 22], fill=p["ink"], width=2)
    d.polygon([(cx - 5, cy + 22), (cx + 5, cy + 22), (cx, cy + 30)],
              fill=p["accent"])


def scene_explosion(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _smoke(d, x + int(w * 0.6), y + int(h * 0.4), 14, p)
    d.rectangle([x + int(w * 0.15), y + int(h * 0.55), x + int(w * 0.4),
                 y + int(h * 0.78)], fill=p["ink"])
    d.rectangle([x + int(w * 0.55), y + int(h * 0.62), x + int(w * 0.85),
                 y + int(h * 0.78)], fill=p["ink"])
    _burst(d, x + w // 2, y + int(h * 0.42), 22, p)


def scene_storm(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _cloud(d, x + int(w * 0.1), y + int(h * 0.18), 46, p)
    _cloud(d, x + int(w * 0.55), y + int(h * 0.1), 38, p)
    for i in range(6):
        xx = x + 12 + i * 12
        d.line([xx, y + int(h * 0.5), xx - 5, y + int(h * 0.72)],
               fill=p["rain"], width=2)
    d.polygon([(x + int(w * 0.45), y + int(h * 0.42)),
               (x + int(w * 0.38), y + int(h * 0.66)),
               (x + int(w * 0.48), y + int(h * 0.66)),
               (x + int(w * 0.4), y + int(h * 0.85))],
              fill=p["sun"])


def scene_shopping(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _sun(d, x, y, w, h, p)
    bx, by = x + int(w * 0.28), y + int(h * 0.3)
    bw, bh = int(w * 0.44), int(h * 0.45)
    d.rectangle([bx, by, bx + bw, by + bh], fill=p["accent"])
    d.rectangle([bx, by, bx + bw, by + 8], fill=p["sun"])
    d.arc([bx + 8, by - 12, bx + bw - 8, by + 12], 180, 360,
          fill=p["ink"], width=3)
    d.ellipse([bx + bw - 12, by + bh - 12, bx + bw + 4, by + bh + 4],
              fill=p["sun"])
    d.text((bx + bw - 9, by + bh - 10), "%", fill=p["ink"])


def scene_chart(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    d.line([x + 12, y + 14, x + 12, y + h - 16], fill=p["ink"], width=2)
    d.line([x + 12, y + h - 16, x + w - 10, y + h - 16],
           fill=p["ink"], width=2)
    for i, bh in enumerate((10, 18, 14, 26, 34)):
        bx = x + 20 + i * 13
        d.rectangle([bx, y + h - 16 - bh, bx + 8, y + h - 16],
                    fill=p["bar"] if i % 2 else p["accent"])
    d.line([x + 16, y + h - 30, x + w - 14, y + 18], fill=p["sun"],
           width=3)


def scene_missile(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _cloud(d, x + int(w * 0.6), y + int(h * 0.14), 30, p)
    cx, cy = x + w // 2, y + int(h * 0.5)
    d.polygon([(cx, cy - 26), (cx + 8, cy - 8), (cx + 8, cy + 14),
               (cx, cy + 22), (cx - 8, cy + 14), (cx - 8, cy - 8)],
              fill=p["ink"])
    d.polygon([(cx - 14, cy + 10), (cx - 8, cy + 4), (cx - 8, cy + 16)],
              fill=p["accent"])
    d.polygon([(cx + 14, cy + 10), (cx + 8, cy + 4), (cx + 8, cy + 16)],
              fill=p["accent"])
    d.polygon([(cx - 5, cy + 22), (cx + 5, cy + 22), (cx, cy + 34)],
              fill=p["sun"])
    d.line([cx - 26, cy + 30, cx - 34, cy + 30], fill=p["smoke"], width=2)
    d.line([cx + 26, cy + 30, cx + 34, cy + 30], fill=p["smoke"], width=2)


def scene_volcano(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _sun(d, x, y, w, h, p)
    d.polygon([(x + 8, y + h - 18), (x + w // 2, y + int(h * 0.3)),
               (x + w - 8, y + h - 18)], fill=p["mount"])
    d.polygon([(x + w // 2 - 10, y + int(h * 0.3)),
               (x + w // 2 + 10, y + int(h * 0.3)),
               (x + w // 2 + 4, y + int(h * 0.45)),
               (x + w // 2 - 4, y + int(h * 0.45))], fill=p["lava"])
    d.polygon([(x + w // 2 - 3, y + int(h * 0.45)),
               (x + w // 2 + 3, y + int(h * 0.45)),
               (x + w // 2 + 8, y + int(h * 0.72)),
               (x + w // 2 - 8, y + int(h * 0.72))], fill=p["lava"])
    _smoke(d, x + int(w * 0.42), y + int(h * 0.3), 12, p)


def scene_tanker(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    _sun(d, x, y, w, h, p)
    d.rectangle([x + int(w * 0.18), y + int(h * 0.42), x + int(w * 0.82),
                 y + int(h * 0.6)], fill=p["ink"])
    d.rectangle([x + int(w * 0.3), y + int(h * 0.3), x + int(w * 0.42),
                 y + int(h * 0.42)], fill=p["ink"])
    d.rectangle([x + int(w * 0.58), y + int(h * 0.34), x + int(w * 0.66),
                 y + int(h * 0.42)], fill=p["accent"])
    d.polygon([(x + int(w * 0.18), y + int(h * 0.6)),
               (x + int(w * 0.82), y + int(h * 0.6)),
               (x + int(w * 0.72), y + int(h * 0.74)),
               (x + int(w * 0.28), y + int(h * 0.74))], fill=p["ink"])
    _waves(d, x + 6, y + int(h * 0.76), w - 12, p)


def scene_fire(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    d.rectangle([x + int(w * 0.2), y + int(h * 0.55), x + int(w * 0.8),
                 y + int(h * 0.78)], fill=p["ink"])
    for i in range(3):
        d.rectangle([x + int(w * 0.28) + i * 14, y + int(h * 0.6),
                     x + int(w * 0.28) + i * 14 + 8,
                     y + int(h * 0.6) + 8], fill=p["sun"])
    _smoke(d, x + int(w * 0.55), y + int(h * 0.4), 14, p)
    cx = x + w // 2
    d.polygon([(cx - 18, y + int(h * 0.55)), (cx, y + int(h * 0.18)),
               (cx + 18, y + int(h * 0.55))], fill=p["accent"])
    d.polygon([(cx - 9, y + int(h * 0.55)), (cx, y + int(h * 0.34)),
               (cx + 9, y + int(h * 0.55))], fill=p["sun"])


def scene_chess(d, x, y, w, h, p):
    d.rectangle([x, y, x + w, y + h], fill=p["sky"])
    s = min(w, h) // 8
    ox, oy = x + (w - s * 6) // 2, y + (h - s * 6) // 2
    for r in range(6):
        for c in range(6):
            col = p["card"] if (r + c) % 2 == 0 else p["ink"]
            d.rectangle([ox + c * s, oy + r * s, ox + (c + 1) * s,
                         oy + (r + 1) * s], fill=col)
    d.ellipse([ox + s, oy + s, ox + 2 * s, oy + 2 * s], fill=p["accent"])
    d.ellipse([ox + 4 * s, oy + 3 * s, ox + 5 * s, oy + 4 * s],
              fill=p["sun"])
    d.rectangle([ox + s, oy + s, ox + 2 * s, oy + 2 * s],
                outline=p["ink"], width=1)


def scene_tennis(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    d.rectangle([x + 8, y + int(h * 0.5), x + w - 8, y + int(h * 0.78)],
                fill=p["court"])
    d.line([x + 8, y + int(h * 0.5), x + w - 8, y + int(h * 0.5)],
           fill=p["white"], width=2)
    d.line([x + w // 2, y + int(h * 0.5), x + w // 2, y + int(h * 0.78)],
           fill=p["white"], width=2)
    d.line([x + int(w * 0.3), y + int(h * 0.32), x + int(w * 0.7),
            y + int(h * 0.32)], fill=p["ink"], width=2)
    d.ellipse([x + int(w * 0.62), y + int(h * 0.2), x + int(w * 0.62) + 16,
               y + int(h * 0.2) + 16], fill=p["sun"])
    d.arc([x + int(w * 0.62), y + int(h * 0.2), x + int(w * 0.62) + 16,
           y + int(h * 0.2) + 16], 200, 340, fill=p["white"], width=2)


def scene_court(d, x, y, w, h, p):
    _sky(d, x, y, w, h, p)
    d.rectangle([x + int(w * 0.15), y + int(h * 0.3), x + int(w * 0.85),
                 y + int(h * 0.38)], fill=p["ink"])
    for i in range(3):
        cx = x + int(w * (0.25 + i * 0.25))
        d.rectangle([cx - 4, y + int(h * 0.38), cx + 4, y + int(h * 0.72)],
                    fill=p["ink"])
    d.rectangle([x + int(w * 0.12), y + int(h * 0.72), x + int(w * 0.88),
                 y + int(h * 0.78)], fill=p["ink"])
    d.line([x + w // 2 - 14, y + int(h * 0.2), x + w // 2 + 14,
            y + int(h * 0.2)], fill=p["ink"], width=3)
    d.line([x + w // 2, y + int(h * 0.2), x + w // 2, y + int(h * 0.3)],
           fill=p["ink"], width=3)


def scene_globe(d, x, y, w, h, p):
    d.rectangle([x, y, x + w, y + h], fill=p["sky"])
    cx, cy, r = x + w // 2, y + h // 2, min(w, h) // 2 - 6
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=p["ocean"])
    d.ellipse([cx - r // 2, cy - r // 3, cx + r // 4, cy + r // 3],
              fill=p["land"])
    d.ellipse([cx + r // 3, cy + r // 4, cx + r // 2, cy + r // 2],
              fill=p["land"])
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=p["ink"], width=2)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360,
          fill=p["white"], width=1)


SCENES = {
    "drone": scene_drone, "explosion": scene_explosion,
    "storm": scene_storm, "shopping": scene_shopping,
    "chart": scene_chart, "missile": scene_missile,
    "volcano": scene_volcano, "tanker": scene_tanker,
    "fire": scene_fire, "chess": scene_chess,
    "tennis": scene_tennis, "court": scene_court,
    "globe": scene_globe,
}


def draw_scene(d, kind, x, y, w, h, palette):
    fn = SCENES.get(kind, scene_globe)
    fn(d, x, y, w, h, palette)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=palette["ink"],
                width=1)
