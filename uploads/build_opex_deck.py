from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from PIL import Image
import os

# ── Palette: navy / steel-blue / grey / white ──────────────────
NAVY       = RGBColor(0x0F, 0x1F, 0x35)   # deep navy bg
PANEL      = RGBColor(0x16, 0x28, 0x40)   # left-panel navy
BLUE       = RGBColor(0x3B, 0x82, 0xC4)   # steel-blue accent
BLUE_LT    = RGBColor(0x60, 0xA5, 0xD8)   # lighter blue
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
OFF_WHITE  = RGBColor(0xE8, 0xEF, 0xF6)
GREY       = RGBColor(0x8B, 0xA4, 0xBC)   # blue-grey secondary text
GREY_DK    = RGBColor(0x2A, 0x3E, 0x55)   # dividers / card bg
CARD_BG    = RGBColor(0x17, 0x2A, 0x42)   # learning cards

LOGO_DIR  = os.path.join(os.path.dirname(__file__), "logos")
PROC_DIR  = os.path.join(os.path.dirname(__file__), "logos_processed")
os.makedirs(PROC_DIR, exist_ok=True)

# All companies — name + filename
COMPANIES = [
    ("Amazon",              "amazon.com.png"),
    ("APM Terminals",       "apmterminals.com.png"),
    ("ASML",                None),
    ("BASF",                "basf.com.png"),
    ("Bilfinger",           "Bilfinger_Logo_horizontal.jpg"),
    ("Bizagi",              "bizagi.com.png"),
    ("BTA Food & Services", "bta_food_and_services_group_logo.jpg"),
    ("CCC Group",           "ccc group.jpg"),
    ("Columbia Sportswear", "columbia.com.png"),
    ("European XFEL",       "European_XFEL_logo.svg.png"),
    ("Evonik",              "evonik.com.png"),
    ("exceedium",           "exceedium.com.png"),
    ("FedEx",               "fedex.com.png"),
    ("HelloFresh",          "HelloFresh_Logo.png"),
    ("John Crane",          "John_Crane_Inc._Logo.png"),
    ("Kaizen Institute",    "kaizen.com.png"),
    ("Kovant",              "kovant.com.logo.jpg"),
    ("Linde",               "linde.com.png"),
    ("MediaMarktSaturn",    "mediamarktsaturn.com.png"),
    ("NORMA Group",         "NORMA_LOGO-2.png"),
    ("Pandatron",           "pandatron.de.png"),
    ("PPG",                 "ppg.com.png"),
    ("Shell",               "shell.com.png"),
    ("Six Sigma Inst.",     "sixsigma-institute.org.png"),
    ("Sixt",                "sixt.png"),
    ("Solidelectron",       "solideletron.png"),
    ("Specialized",         "specialized.com.png"),
    ("Sportradar",          "Sportradar_Logo.png"),
]

# Most recognisable for the logo composition on slide 1 (bottom right)
FEATURE_LOGOS = [
    "amazon.com.png", "shell.com.png", "fedex.com.png", "basf.com.png",
    "linde.com.png",  "HelloFresh_Logo.png", "Bilfinger_Logo_horizontal.jpg",
    "columbia.com.png",
]

PHOTOS = {
    1: os.path.join(LOGO_DIR, "photo 1.jpg"),
    2: os.path.join(LOGO_DIR, "photo 2.jpg"),
    3: os.path.join(LOGO_DIR, "photo 3.jpg"),
}

LEARNINGS = [
    ("OutSystems visibility",
     "Only a few attendees had heard of OutSystems — a reminder of how much "
     "brand reach still matters outside the tech bubble."),
    ("Agents as team members",
     '"Agents are your new team members" — Somil Gupta (Kovant). '
     "Multiple speakers confirmed agents running as process operators "
     "with human oversight is where the industry is heading."),
    ("AI trust gap",
     "A general feeling of lack of trust in AI persisted. "
     "Only a handful of presentations showed AI making a measurable "
     "difference in their organisations."),
    ("We are ahead on enablement",
     "Compared with non-tech organisations, our AI enablement level "
     "is already above average. We have a head start — the question "
     "is whether we use it."),
    ("ASML x Kaizen hypergrowth",
     "ASML leveraged Kaizen as their hypergrowth strategy from day one. "
     "A powerful proof point: continuous improvement frameworks scale from startup to global leader."),
]

PE_POINTS = [
    ("Validate the direction",
     "The 'agents as process operators' framing aligns exactly with Method 1 "
     "(AI Transformation). OPEX 2026 confirms we are building toward the right future."),
    ("Leverage the head start",
     "Most organisations are still figuring out AI trust. Now is the time to "
     "move from exploration to measurable impact."),
    ("Build trust through results",
     "The trust gap seen at OPEX is real here too. Our answer is demonstrated "
     "outcomes — visible wins tied to KPIs, not more tooling."),
    ("Continuous improvement scales",
     "ASML's Kaizen story is our story too. The frameworks we are building now "
     "are the foundation for how PE scales with the company."),
]

# ── Helpers ────────────────────────────────────────────────────

def prepare_logo(filename, out_size=(240, 100)):
    dst = os.path.join(PROC_DIR, os.path.splitext(filename)[0] + ".png")
    if os.path.exists(dst):
        return dst
    src = os.path.join(LOGO_DIR, filename)
    try:
        img = Image.open(src).convert("RGBA")
        img.thumbnail((out_size[0] - 16, out_size[1] - 12), Image.LANCZOS)
        canvas = Image.new("RGBA", out_size, (255, 255, 255, 255))
        x = (out_size[0] - img.width) // 2
        y = (out_size[1] - img.height) // 2
        canvas.paste(img, (x, y), img)
        canvas.convert("RGB").save(dst, "PNG")
        return dst
    except Exception as e:
        print(f"  WARNING {filename}: {e}")
        return None

def prepare_photo(path, max_w=900, max_h=600):
    name = os.path.basename(path)
    dst  = os.path.join(PROC_DIR, name + ".proc.jpg")
    if os.path.exists(dst):
        return dst
    try:
        img = Image.open(path).convert("RGB")
        img.thumbnail((max_w, max_h), Image.LANCZOS)
        img.save(dst, "JPEG", quality=90)
        return dst
    except Exception as e:
        print(f"  WARNING photo {path}: {e}")
        return None

def add_rect(slide, l, t, w, h, fill=None, line=False):
    s = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    if fill:
        s.fill.solid(); s.fill.fore_color.rgb = fill
    else:
        s.fill.background()
    if not line:
        s.line.fill.background()
    return s

def add_text(slide, l, t, w, h, text, size, bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, wrap=True):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = wrap
    p  = tf.paragraphs[0]; p.alignment = align
    r  = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
    return tb

def add_para(tf, text, size, bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, space_before=4):
    p = tf.add_paragraph()
    p.alignment = align; p.space_before = Pt(space_before)
    r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
    return p

# ── Pre-process assets ─────────────────────────────────────────
print("Processing logos...")
logo_cache = {}
for name, fn in COMPANIES:
    if fn:
        logo_cache[fn] = prepare_logo(fn)

feature_processed = []
for fn in FEATURE_LOGOS:
    p = prepare_logo(fn, out_size=(280, 100))
    feature_processed.append(p)

print("Processing photos...")
photo_cache = {}
for k, path in PHOTOS.items():
    photo_cache[k] = prepare_photo(path) if os.path.exists(path) else None
    print(f"  Photo {k}: {'OK' if photo_cache[k] else 'NOT FOUND'}")

# ── Presentation setup ─────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

# ══════════════════════════════════════════════════════════════
# SLIDE 1 — What was OPEX 2026 + who was there
# ══════════════════════════════════════════════════════════════
s1 = prs.slides.add_slide(blank)
add_rect(s1, 0, 0, 13.33, 7.5, fill=NAVY)

PANEL_W = 3.8
add_rect(s1, 0, 0, PANEL_W, 7.5, fill=PANEL)
add_rect(s1, 0, 0, 0.05, 7.5, fill=BLUE)

# Panel header
add_text(s1, 0.18, 0.20, PANEL_W - 0.25, 0.32,
         "WHO WAS THERE", 7.5, bold=True, color=BLUE_LT)

# Company names — 2-col list
names   = [c[0] for c in COMPANIES]
cols    = 2
rows    = (len(names) + cols - 1) // cols
col_w   = (PANEL_W - 0.25) / cols
start_x = 0.15
start_y = 0.60
row_h   = (7.5 - start_y - 0.15) / rows

for i, name in enumerate(names):
    col = i % cols
    row = i // cols
    cx  = start_x + col * col_w
    cy  = start_y + row * row_h
    # subtle separator line
    add_rect(s1, cx, cy, col_w - 0.06, 0.01, fill=GREY_DK)
    tb = s1.shapes.add_textbox(
        Inches(cx + 0.04), Inches(cy + 0.03),
        Inches(col_w - 0.10), Inches(row_h - 0.04)
    )
    tf = tb.text_frame; tf.word_wrap = False
    p  = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
    r  = p.add_run(); r.text = name
    r.font.size  = Pt(8.0)
    r.font.color.rgb = OFF_WHITE

# Right content area
RX = PANEL_W + 0.40
RW = 13.33 - RX - 0.35

add_rect(s1, RX, 0.30, 0.90, 0.04, fill=BLUE)
add_text(s1, RX, 0.44, RW, 0.28,
         "MUNICH, GERMANY  ·  MAY 2026", 8, color=GREY)

# Title
tb = s1.shapes.add_textbox(Inches(RX), Inches(0.76), Inches(RW), Inches(1.30))
tf = tb.text_frame; tf.word_wrap = True
p  = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
r  = p.add_run()
r.text = "Operational Excellence &\nProcess Transformation Summit"
r.font.size = Pt(26); r.font.bold = True; r.font.color.rgb = WHITE

add_rect(s1, RX, 2.14, RW, 0.02, fill=GREY_DK)

# Body bullets
tb = s1.shapes.add_textbox(Inches(RX), Inches(2.28), Inches(RW * 0.56), Inches(3.20))
tf = tb.text_frame; tf.word_wrap = True
bullets = [
    ("3-day international summit",
     "Process transformation, continuous improvement, and operational excellence in the AI era."),
    ("BMW Museum opening night",
     "Day 1 at the BMW Museum — a live case study in precision and innovation culture."),
    ("2 full days of sessions",
     "Workshops, keynotes, and peer-led success stories from global organisations."),
    ("27 organisations in the room",
     "Across industry, logistics, chemicals, tech, manufacturing, and beyond."),
]
first = True
for title_t, body_t in bullets:
    if not first:
        sp = tf.add_paragraph(); sp.space_before = Pt(7); sp.add_run().text = ""
    first = False
    pt = tf.add_paragraph(); pt.space_before = Pt(1)
    rt = pt.add_run(); rt.text = f"›  {title_t}"
    rt.font.size = Pt(10.5); rt.font.bold = True; rt.font.color.rgb = WHITE
    pb = tf.add_paragraph(); pb.space_before = Pt(1)
    rb = pb.add_run(); rb.text = f"   {body_t}"
    rb.font.size = Pt(9); rb.font.color.rgb = GREY

# ── Featured logo strip — bottom right ─────────────────────────
STRIP_X = RX + RW * 0.58
STRIP_Y = 2.30
LOGO_W  = (13.33 - STRIP_X - 0.25) / 2 - 0.08
LOGO_H  = 0.72
GAP_X   = 0.10
GAP_Y   = 0.10

add_text(s1, STRIP_X, STRIP_Y - 0.28, 4.0, 0.24,
         "FEATURED PARTICIPANTS", 7, color=BLUE_LT, bold=True)

for i, lp in enumerate(feature_processed):
    col = i % 2
    row = i // 2
    lx  = STRIP_X + col * (LOGO_W + GAP_X)
    ly  = STRIP_Y + row * (LOGO_H + GAP_Y)
    add_rect(s1, lx, ly, LOGO_W, LOGO_H, fill=WHITE)
    if lp:
        pad = 0.06
        s1.shapes.add_picture(
            lp, Inches(lx + pad), Inches(ly + pad),
            width=Inches(LOGO_W - pad * 2), height=Inches(LOGO_H - pad * 2)
        )

add_text(s1, 12.9, 7.22, 0.4, 0.24, "1", 8, color=GREY, align=PP_ALIGN.RIGHT)


# ══════════════════════════════════════════════════════════════
# SLIDE 2 — Key Learnings + Photos 2 & 3
# ══════════════════════════════════════════════════════════════
s2 = prs.slides.add_slide(blank)
add_rect(s2, 0, 0, 13.33, 7.5, fill=NAVY)
add_rect(s2, 0, 0, 13.33, 0.06, fill=BLUE)

add_text(s2, 0.45, 0.18, 5.0, 0.28,
         "OPEX 2026  ·  KEY LEARNINGS", 7.5, color=BLUE_LT, bold=True)

tb = s2.shapes.add_textbox(Inches(0.45), Inches(0.50), Inches(7.5), Inches(0.80))
tf = tb.text_frame; p = tf.paragraphs[0]; r = p.add_run()
r.text = "What I Brought Back"
r.font.size = Pt(28); r.font.bold = True; r.font.color.rgb = WHITE

add_rect(s2, 0.45, 1.38, 12.4, 0.02, fill=GREY_DK)

# Left: learning cards (stacked, full height)
CARD_W = 7.60
CARD_H = 1.12
CARD_X = 0.45
GAP    = 0.10

for i, (label, body) in enumerate(LEARNINGS):
    cy = 1.52 + i * (CARD_H + GAP)
    add_rect(s2, CARD_X, cy, CARD_W, CARD_H, fill=CARD_BG)
    add_rect(s2, CARD_X, cy, 0.04, CARD_H, fill=BLUE)

    num = s2.shapes.add_textbox(
        Inches(CARD_X + 0.12), Inches(cy + 0.10),
        Inches(0.32), Inches(0.32)
    )
    ntf = num.text_frame; np_ = ntf.paragraphs[0]
    np_.alignment = PP_ALIGN.CENTER
    nr = np_.add_run(); nr.text = str(i + 1)
    nr.font.size = Pt(10); nr.font.bold = True; nr.font.color.rgb = BLUE_LT

    ltb = s2.shapes.add_textbox(
        Inches(CARD_X + 0.52), Inches(cy + 0.08),
        Inches(CARD_W - 0.62), Inches(0.32)
    )
    ltf = ltb.text_frame; lp = ltf.paragraphs[0]
    lr = lp.add_run(); lr.text = label
    lr.font.size = Pt(10); lr.font.bold = True; lr.font.color.rgb = WHITE

    btb = s2.shapes.add_textbox(
        Inches(CARD_X + 0.52), Inches(cy + 0.42),
        Inches(CARD_W - 0.62), Inches(CARD_H - 0.50)
    )
    btf = btb.text_frame; btf.word_wrap = True
    bp = btf.paragraphs[0]
    br = bp.add_run(); br.text = body
    br.font.size = Pt(8.5); br.font.color.rgb = GREY

# Right: Photos 2 & 3 stacked
PH_X  = CARD_X + CARD_W + 0.22
PH_W  = 13.33 - PH_X - 0.25
PH_H  = (7.5 - 1.52 - 0.30) / 2 - 0.08

for slot, photo_key in [(0, 2), (1, 3)]:
    py = 1.52 + slot * (PH_H + 0.14)
    ph = photo_cache.get(photo_key)
    if ph:
        s2.shapes.add_picture(ph, Inches(PH_X), Inches(py),
                              width=Inches(PH_W), height=Inches(PH_H))
        # subtle overlay label
        add_rect(s2, PH_X, py + PH_H - 0.28, PH_W, 0.28,
                 fill=RGBColor(0x0F, 0x1F, 0x35))
    else:
        add_rect(s2, PH_X, py, PH_W, PH_H, fill=GREY_DK)

add_text(s2, 12.9, 7.22, 0.4, 0.24, "2", 8, color=GREY, align=PP_ALIGN.RIGHT)


# ══════════════════════════════════════════════════════════════
# SLIDE 3 — What This Means for PE + Photo 1
# ══════════════════════════════════════════════════════════════
s3 = prs.slides.add_slide(blank)
add_rect(s3, 0, 0, 13.33, 7.5, fill=NAVY)
add_rect(s3, 0, 0, 0.05, 7.5, fill=BLUE)

add_text(s3, 0.30, 0.20, 5.0, 0.28,
         "OPEX 2026  ·  IMPLICATIONS", 7.5, color=BLUE_LT, bold=True)

tb = s3.shapes.add_textbox(Inches(0.30), Inches(0.52), Inches(7.8), Inches(0.95))
tf = tb.text_frame; tf.word_wrap = True
p  = tf.paragraphs[0]; r = p.add_run()
r.text = "What This Means for Process Engineering"
r.font.size = Pt(26); r.font.bold = True; r.font.color.rgb = WHITE

add_rect(s3, 0.30, 1.54, 8.10, 0.02, fill=GREY_DK)

# 2x2 implication grid
IMP_W  = 3.90
IMP_H  = 2.30
IGAP_X = 0.22
IGAP_Y = 0.18
IX1    = 0.30
IX2    = IX1 + IMP_W + IGAP_X
IY1    = 1.68
IY2    = IY1 + IMP_H + IGAP_Y

for i, (label, body) in enumerate(PE_POINTS):
    ix = IX1 if i % 2 == 0 else IX2
    iy = IY1 if i < 2 else IY2
    add_rect(s3, ix, iy, IMP_W, IMP_H, fill=CARD_BG)
    add_rect(s3, ix, iy, IMP_W, 0.04, fill=BLUE)

    ltb = s3.shapes.add_textbox(
        Inches(ix + 0.18), Inches(iy + 0.16),
        Inches(IMP_W - 0.26), Inches(0.36)
    )
    ltf = ltb.text_frame; lp = ltf.paragraphs[0]
    lr = lp.add_run(); lr.text = label
    lr.font.size = Pt(11); lr.font.bold = True; lr.font.color.rgb = WHITE

    btb = s3.shapes.add_textbox(
        Inches(ix + 0.18), Inches(iy + 0.56),
        Inches(IMP_W - 0.26), Inches(IMP_H - 0.65)
    )
    btf = btb.text_frame; btf.word_wrap = True
    bp = btf.paragraphs[0]
    br = bp.add_run(); br.text = body
    br.font.size = Pt(9.5); br.font.color.rgb = GREY

# Right: Photo 1 — full height
P1_X = IX2 + IMP_W + 0.28
P1_W = 13.33 - P1_X - 0.20
P1_Y = 0.20
P1_H = 7.5 - P1_Y - 0.20

ph1 = photo_cache.get(1)
if ph1:
    s3.shapes.add_picture(ph1, Inches(P1_X), Inches(P1_Y),
                          width=Inches(P1_W), height=Inches(P1_H))
else:
    add_rect(s3, P1_X, P1_Y, P1_W, P1_H, fill=GREY_DK)

add_text(s3, 12.9, 7.22, 0.4, 0.24, "3", 8, color=GREY, align=PP_ALIGN.RIGHT)


# ── Save ───────────────────────────────────────────────────────
out = r"C:\Users\vbr\Desktop\Veriski\Veriski\uploads\OPEX2026_ProcessEngineering.pptx"
prs.save(out)
print(f"\nSaved: {out}")
