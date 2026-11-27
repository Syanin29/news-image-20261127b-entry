# Renderer: draws the 1024x1024 front page from stories.py.
# Two layouts (A frontpage, B ledger) x three palettes (paper, dark,
# tabloid) = six variants. Deterministic: no randomness, no time,
# no network. PNG is written by Pillow with fixed settings.

from PIL import Image, ImageDraw, ImageFont

import scenes
import stories

W = H = 1024
M = 12  # outer margin


PALETTES = {
    "paper": dict(bg="#F7F2E7", ink="#1B2A4A", accent="#C0392B",
                  sky="#BFD9E8", sky2="#8FB8D4", ground="#D9C9A8",
                  sun="#F2B705", sun2="#F7D154", white="#FFFFFF",
                  smoke="#9AA5B1", wave="#2E6F9E", wave2="#7FB3D5",
                  bar="#2E6F9E", mount="#5D4037", lava="#E64A19",
                  ocean="#B7D3E8", land="#8FAE6B", court="#3E7A4E",
                  rain="#2E6F9E", card="#FFFFFF", muted="#5A6B7F",
                  band="#1B2A4A", bandtext="#F7F2E7"),
    "dark": dict(bg="#0F1B2D", ink="#E8EDF3", accent="#FF6B4A",
                 sky="#1E3A5F", sky2="#274B73", ground="#2A2118",
                 sun="#FFC53D", sun2="#FFE08A", white="#E8EDF3",
                 smoke="#8A97A8", wave="#4A90C2", wave2="#7FB3D5",
                 bar="#4A90C2", mount="#3D2C22", lava="#FF7A45",
                 ocean="#1E4A73", land="#5E8F4E", court="#2F6B3E",
                 rain="#7FB3D5", card="#16273E", muted="#9AA8BC",
                 band="#E8EDF3", bandtext="#0F1B2D"),
    "tabloid": dict(bg="#FFF8E7", ink="#111111", accent="#D40000",
                    sky="#CFE3F2", sky2="#A8C8E4", ground="#E8D9B0",
                    sun="#FFB300", sun2="#FFD54F", white="#FFFFFF",
                    smoke="#8D9BA5", wave="#1F5F8B", wave2="#6FA8CF",
                    bar="#1F5F8B", mount="#4E342E", lava="#FF5722",
                    ocean="#A9C8E2", land="#7CA35A", court="#2E7D32",
                    rain="#1F5F8B", card="#FFFFFF", muted="#6B7280",
                    band="#D40000", bandtext="#FFF8E7"),
}

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def load_fonts():
    try:
        bold = ImageFont.truetype(FONT_PATHS[0], 20)
        reg = ImageFont.truetype(FONT_PATHS[1], 20)
        ok = True
    except Exception:
        ok = False
    if ok:
        def f(size, b=False):
            return ImageFont.truetype(FONT_PATHS[0] if b else FONT_PATHS[1],
                                      size)
    else:
        try:
            def f(size, b=False):
                return ImageFont.load_default(size=size)
        except Exception:
            def f(size, b=False):
                return ImageFont.load_default()
    return dict(mast=lambda: f(33, True), kick=lambda: f(13, True),
                lead=lambda: f(13, False), kpi=lambda: f(25, True),
                kpilab=lambda: f(10, False), regbar=lambda: f(11, True),
                fields=lambda: f(10, False), hhead=lambda: f(15, True),
                hbody=lambda: f(11, False), hsrc=lambda: f(9, True),
                shead=lambda: f(12, True), sbody=lambda: f(10, False),
                ssrc=lambda: f(8, True), lst=lambda: f(9, False),
                lhead=lambda: f(12, True), bhead=lambda: f(12, True),
                bbody=lambda: f(10, False), bsmall=lambda: f(9, False),
                badge=lambda: f(13, True))


def wrap(d, text, font, width, max_lines=None):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
            if max_lines and len(lines) >= max_lines:
                break
    if cur and (not max_lines or len(lines) < max_lines):
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, font, fill, leading=None):
    lh = leading or int(font.size * 1.25)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y


def trunc(d, text, font, width):
    if d.textlength(text, font=font) <= width:
        return text
    while text and d.textlength(text + "...", font=font) > width:
        text = text[:-1]
    return text + "..."


def status_color(p, status):
    return {"CONFIRMED": "#1E7A34", "REPORTED": "#8A6D00",
            "CLAIM": "#8A4B00", "ONGOING": "#B03A2E"}.get(status, "#555555")


# ---------------------------------------------------------------- continents
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70),
     (-75, 62), (-60, 55), (-55, 47), (-65, 44), (-75, 38), (-80, 32),
     (-85, 29), (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40),
     (-140, 60), (-160, 58), (-168, 66)],
    [(-80, 10), (-60, 5), (-50, 0), (-35, -8), (-40, -20), (-48, -28),
     (-58, -35), (-65, -45), (-70, -52), (-73, -40), (-75, -20),
     (-80, -5), (-80, 10)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 58), (10, 57), (18, 56),
     (21, 55), (28, 60), (30, 70), (40, 68), (45, 60), (40, 55), (35, 48),
     (30, 45), (23, 40), (19, 42), (12, 44), (8, 44), (3, 42), (-2, 37),
     (-10, 36)],
    [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (40, 15), (43, 11),
     (51, 10), (48, 0), (40, -10), (35, -20), (32, -28), (20, -35),
     (15, -30), (12, -18), (9, -2), (9, 4), (-8, 5), (-15, 11),
     (-17, 15), (-16, 20), (-10, 30), (-6, 35)],
    [(40, 68), (50, 70), (60, 70), (70, 72), (80, 73), (100, 77),
     (110, 74), (130, 72), (140, 72), (160, 66), (162, 60), (158, 52),
     (142, 45), (140, 40), (130, 42), (127, 38), (122, 32), (120, 25),
     (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (85, 20),
     (80, 15), (75, 8), (70, 23), (65, 25), (58, 26), (55, 26), (50, 28),
     (48, 30), (45, 32), (42, 35), (40, 38), (40, 45), (42, 55),
     (40, 68)],
    [(113, -22), (114, -30), (115, -35), (124, -33), (129, -32),
     (137, -35), (140, -38), (147, -39), (150, -37), (153, -32),
     (153, -27), (146, -19), (142, -11), (136, -12), (132, -12),
     (126, -14), (122, -17), (118, -20), (113, -22)],
]


def draw_map(d, x, y, w, h, p, fonts):
    d.rectangle([x, y, x + w, y + h], fill=p["ocean"])
    d.rectangle([x, y, x + w, y + 24], fill=p["ink"])
    d.text((x + 8, y + 5), "THE WORLD - 13 STORIES PINNED",
           font=fonts["lhead"](), fill=p["card"])
    y0, h0 = y + 24, h - 24
    for gx in range(1, 6):
        xx = x + w * gx // 6
        d.line([xx, y0, xx, y0 + h0], fill=p["white"], width=1)
    for gy in range(1, 4):
        yy = y0 + h0 * gy // 4
        d.line([x, yy, x + w, yy], fill=p["white"], width=1)
    for poly in CONTINENTS:
        pts = [(x + (lon + 180) / 360 * w, y0 + (90 - lat) / 180 * h0)
               for lon, lat in poly]
        d.polygon(pts, fill=p["land"], outline=p["ink"])
    used = []
    for num, (lon, lat) in sorted(stories.PINS.items()):
        px = x + (lon + 180) / 360 * w
        py = y0 + (90 - lat) / 180 * h0
        tx, ty = px, py
        for ox, oy in used:
            if abs(px - ox) < 18 and abs(py - oy) < 18:
                px += 13
                py -= 11
        used.append((px, py))
        if (px, py) != (tx, ty):
            d.line([tx, ty, px, py], fill=p["ink"], width=1)
        r = 10
        d.ellipse([px - r, py - r, px + r, py + r], fill=p["accent"],
                  outline=p["white"], width=2)
        t = str(num)
        tw = d.textlength(t, font=fonts["badge"]())
        d.text((px - tw / 2, py - 7), t, font=fonts["badge"](),
               fill=p["white"])


# ---------------------------------------------------------------- sections
def draw_masthead(d, p, fonts):
    d.rectangle([M, M, W - M, 96], fill=p["band"])
    d.text((M + 12, M + 8), stories.DATE_LINE, font=fonts["mast"](),
           fill=p["bandtext"])
    d.text((M + 12, M + 50), stories.TITLE, font=fonts["kick"](),
           fill=p["bandtext"])
    d.text((M + 12, M + 70), stories.LEAD, font=fonts["lead"](),
           fill=p["bandtext"])


def draw_kpi(d, y, p, fonts):
    n = len(stories.KPI)
    bw = (W - 2 * M - (n - 1) * 8) // n
    for i, (num, lab) in enumerate(stories.KPI):
        x = M + i * (bw + 8)
        d.rectangle([x, y, x + bw, y + 48], fill=p["card"],
                    outline=p["ink"], width=1)
        d.text((x + 8, y + 4), num, font=fonts["kpi"](),
               fill=p["accent"])
        d.text((x + 8, y + 31), lab, font=fonts["kpilab"](),
               fill=p["muted"])
    return y + 48


def draw_regions(d, y, p, fonts):
    parts = ["%s %d" % (name, cnt) for name, cnt in stories.REGIONS]
    d.text((M, y + 4), "  |  ".join(parts), font=fonts["regbar"](),
           fill=p["ink"])
    d.text((M, y + 22), stories.FIELDS, font=fonts["fields"](),
           fill=p["muted"])
    return y + 34


def hero_card(d, x, y, w, h, p, fonts, st):
    num, head, body, src, region, status, kind = st
    d.rectangle([x, y, x + w, y + h], fill=p["card"], outline=p["ink"],
                width=1)
    sh = 96
    scenes.draw_scene(d, kind, x + 1, y + 1, w - 2, sh, p)
    r = 13
    d.ellipse([x + 8, y + 8, x + 8 + 2 * r, y + 8 + 2 * r],
              fill=p["accent"], outline=p["white"], width=2)
    t = str(num)
    tw = d.textlength(t, font=fonts["badge"]())
    d.text((x + 8 + r - tw / 2, y + 8 + 6), t, font=fonts["badge"](),
           fill=p["white"])
    ty = y + sh + 8
    ty = text_block(d, x + 8, ty,
                    wrap(d, head, fonts["hhead"](), w - 16, 2),
                    fonts["hhead"](), p["ink"])
    ty = text_block(d, x + 8, ty + 2,
                    wrap(d, body, fonts["hbody"](), w - 16, 3),
                    fonts["hbody"](), p["muted"])
    stw = d.textlength(status, font=fonts["hsrc"]())
    src_txt = trunc(d, "SOURCE: " + src.upper(), fonts["hsrc"](),
                    w - 16 - stw - 10)
    d.text((x + 8, y + h - 18), src_txt, font=fonts["hsrc"](),
           fill=p["muted"])
    d.text((x + w - 8 - stw, y + h - 18), status, font=fonts["hsrc"](),
           fill=status_color(p, status))


def small_card(d, x, y, w, h, p, fonts, st):
    num, head, body, src, region, status, kind = st
    d.rectangle([x, y, x + w, y + h], fill=p["card"], outline=p["ink"],
                width=1)
    sw = 62
    scenes.draw_scene(d, kind, x + 1, y + 1, sw, h - 2, p)
    r = 11
    d.ellipse([x + 5, y + 5, x + 5 + 2 * r, y + 5 + 2 * r],
              fill=p["accent"], outline=p["white"], width=2)
    t = str(num)
    tw = d.textlength(t, font=fonts["badge"]())
    d.text((x + 5 + r - tw / 2, y + 5 + 4), t, font=fonts["badge"](),
           fill=p["white"])
    tx = x + sw + 8
    ty = y + 6
    ty = text_block(d, tx, ty,
                    wrap(d, head, fonts["shead"](), w - sw - 16, 2),
                    fonts["shead"](), p["ink"])
    ty = text_block(d, tx, ty + 1,
                    wrap(d, body, fonts["sbody"](), w - sw - 16, 2),
                    fonts["sbody"](), p["muted"])
    stw = d.textlength(status, font=fonts["ssrc"]())
    text_w = w - sw - 16
    if text_w >= 200:
        src_txt = trunc(d, "SOURCE: " + src.upper(), fonts["ssrc"](),
                        text_w - stw - 8)
        d.text((tx, y + h - 15), src_txt, font=fonts["ssrc"](),
               fill=p["muted"])
        d.text((x + w - 6 - stw, y + h - 15), status,
               font=fonts["ssrc"](), fill=status_color(p, status))
    else:
        src_txt = trunc(d, "SOURCE: " + src.upper(), fonts["ssrc"](),
                        text_w)
        d.text((tx, y + h - 29), src_txt, font=fonts["ssrc"](),
               fill=p["muted"])
        d.text((x + w - 6 - stw, y + h - 15), status,
               font=fonts["ssrc"](), fill=status_color(p, status))


def hero_card_wide(d, x, y, w, h, p, fonts, st):
    num, head, body, src, region, status, kind = st
    d.rectangle([x, y, x + w, y + h], fill=p["card"], outline=p["ink"],
                width=1)
    sw = 118
    scenes.draw_scene(d, kind, x + 1, y + 1, sw, h - 2, p)
    r = 13
    d.ellipse([x + 8, y + 8, x + 8 + 2 * r, y + 8 + 2 * r],
              fill=p["accent"], outline=p["white"], width=2)
    t = str(num)
    tw = d.textlength(t, font=fonts["badge"]())
    d.text((x + 8 + r - tw / 2, y + 8 + 6), t, font=fonts["badge"](),
           fill=p["white"])
    tx = x + sw + 10
    ty = y + 8
    ty = text_block(d, tx, ty,
                    wrap(d, head, fonts["hhead"](), w - sw - 20, 2),
                    fonts["hhead"](), p["ink"])
    ty = text_block(d, tx, ty + 2,
                    wrap(d, body, fonts["hbody"](), w - sw - 20, 4),
                    fonts["hbody"](), p["muted"])
    stw = d.textlength(status, font=fonts["hsrc"]())
    src_txt = trunc(d, src.upper(), fonts["hsrc"](),
                    w - sw - 20 - stw - 10)
    d.text((tx, y + h - 18), src_txt, font=fonts["hsrc"](),
           fill=p["muted"])
    d.text((x + w - 8 - stw, y + h - 18), status,
           font=fonts["hsrc"](), fill=status_color(p, status))


def draw_list(d, x, y, w, h, p, fonts):
    d.rectangle([x, y, x + w, y + h], fill=p["card"], outline=p["ink"],
                width=1)
    d.text((x + 8, y + 6), "ALSO ON FRIDAY - STORIES 14-50",
           font=fonts["lhead"](), fill=p["ink"])
    d.line([x + 8, y + 26, x + w - 8, y + 26], fill=p["accent"], width=2)
    items = stories.LISTED
    half = (len(items) + 1) // 2
    cols = [items[:half], items[half:]]
    cw = (w - 16) // 2
    for ci, col in enumerate(cols):
        cx = x + 8 + ci * cw
        yy = y + 32
        for num, head, src, region in col:
            suffix = " - " + src
            sw = d.textlength(suffix, font=fonts["lst"]())
            head_txt = trunc(d, "%d. %s" % (num, head),
                             fonts["lst"](), cw - 8 - sw)
            d.text((cx, yy), head_txt, font=fonts["lst"](),
                   fill=p["ink"])
            hw = d.textlength(head_txt, font=fonts["lst"]())
            d.text((cx + hw, yy), suffix, font=fonts["lst"](),
                   fill=p["muted"])
            yy += 12


def draw_bottom(d, y, p, fonts):
    h = 132
    bw = (W - 2 * M - 16) // 3
    boxes = [(M, "THE DAY IN UTC"),
             (M + bw + 8, "DATE CHECK - THESE ARE NOT 27 NOVEMBER"),
             (M + 2 * (bw + 8), "HOW SURE")]
    for x, title in boxes:
        d.rectangle([x, y, x + bw, y + h], fill=p["card"],
                    outline=p["ink"], width=1)
        d.text((x + 8, y + 6), title, font=fonts["bhead"](),
               fill=p["accent"])
        d.line([x + 8, y + 24, x + bw - 8, y + 24], fill=p["accent"],
               width=1)
    x = boxes[0][0]
    yy = y + 30
    for hh, ev in stories.TIMELINE:
        d.text((x + 8, yy), hh, font=fonts["bbody"](), fill=p["accent"])
        d.text((x + 52, yy), trunc(d, ev, fonts["bbody"](), bw - 60),
               font=fonts["bbody"](), fill=p["ink"])
        yy += 15
    d.text((x + 8, yy + 4), "Times first reported, UTC.",
           font=fonts["bsmall"](), fill=p["muted"])
    x = boxes[1][0]
    yy = y + 30
    for when, ev in stories.DATE_CHECK:
        d.text((x + 8, yy), when, font=fonts["bbody"](),
               fill=p["accent"])
        d.text((x + 62, yy), trunc(d, ev, fonts["bbody"](), bw - 70),
               font=fonts["bbody"](), fill=p["ink"])
        yy += 15
    d.text((x + 8, yy + 4), "Left out on purpose: wrong date.",
           font=fonts["bsmall"](), fill=p["muted"])
    x = boxes[2][0]
    yy = y + 30
    for lab, meaning in [
            ("CONFIRMED", "a named source confirms it happened"),
            ("REPORTED", "a named outlet reports it"),
            ("CLAIM", "a person claims it, not verified"),
            ("ONGOING", "still developing at press time")]:
        d.text((x + 8, yy), lab, font=fonts["bbody"](),
               fill=status_color(p, lab))
        d.text((x + 82, yy), meaning, font=fonts["bsmall"](),
               fill=p["muted"])
        yy += 14
    d.text((x + 8, yy + 2),
           "Sources are named on each story. Scenes are drawn",
           font=fonts["bsmall"](), fill=p["muted"])
    d.text((x + 8, yy + 14),
           "illustrations, not photographs. 50 stories verified",
           font=fonts["bsmall"](), fill=p["muted"])
    d.text((x + 8, yy + 26),
           "against BBC, Reuters, AP, NYT and others.",
           font=fonts["bsmall"](), fill=p["muted"])
    return y + h


# ---------------------------------------------------------------- layouts
def layout_a(img, p, fonts):
    d = ImageDraw.Draw(img)
    draw_masthead(d, p, fonts)
    y = draw_kpi(d, 104, p, fonts)
    y = draw_regions(d, y + 6, p, fonts)
    hy, hh = 192, 212
    cw = (W - 2 * M - 16) // 3
    for i, st in enumerate(stories.HERO):
        hero_card(d, M + i * (cw + 8), hy, cw, hh, p, fonts, st)
    sy, sh = 412, 100
    scw = (W - 2 * M - 32) // 5
    for i, st in enumerate(stories.CARDS):
        r, c = divmod(i, 5)
        small_card(d, M + c * (scw + 8), sy + r * (sh + 8), scw, sh,
                   p, fonts, st)
    my = 620
    draw_map(d, M, my, 458, 264, p, fonts)
    draw_list(d, M + 466, my, W - 2 * M - 466, 264, p, fonts)
    draw_bottom(d, 892, p, fonts)


def layout_b(img, p, fonts):
    d = ImageDraw.Draw(img)
    draw_masthead(d, p, fonts)
    y = draw_kpi(d, 104, p, fonts)
    y = draw_regions(d, y + 6, p, fonts)
    hy = 192
    hw = 318
    for i, st in enumerate(stories.HERO):
        hero_card_wide(d, M, hy + i * 142, hw, 134, p, fonts, st)
    gx, gy = M + hw + 8, 192
    gw = (W - M - gx - 8) // 2
    gh = 80
    for i, st in enumerate(stories.CARDS):
        r, c = divmod(i, 2)
        small_card(d, gx + c * (gw + 8), gy + r * (gh + 4), gw, gh,
                   p, fonts, st)
    my = 620
    draw_list(d, M, my, 560, 264, p, fonts)
    draw_map(d, M + 568, my, W - 2 * M - 568, 264, p, fonts)
    draw_bottom(d, 892, p, fonts)


VARIANTS = {
    "A-paper": ("A", "paper"), "A-dark": ("A", "dark"),
    "A-tabloid": ("A", "tabloid"), "B-paper": ("B", "paper"),
    "B-dark": ("B", "dark"), "B-tabloid": ("B", "tabloid"),
}


def render(variant):
    layout, pal = VARIANTS[variant]
    p = PALETTES[pal]
    img = Image.new("RGB", (W, H), p["bg"])
    fonts = load_fonts()
    if layout == "A":
        layout_a(img, p, fonts)
    else:
        layout_b(img, p, fonts)
    return img
