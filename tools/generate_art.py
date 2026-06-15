#!/usr/bin/env python3
"""
Kozen Labs — generative flow-field art.

Inspiration: 浩然 (kōzen). In classical Chinese/Japanese thought 浩然の気
(kōzen no ki) is the "vast, flowing vital spirit" described by Mencius — a
boundless, free-flowing moral energy. The piece renders that idea as a flow
field: many streams threading a single field, distinct yet moving as one.

Deterministic by design (fixed seed, no external deps) so the committed SVG is
reproducible. Run: python3 tools/generate_art.py
"""

import math

# ----- Kozen design tokens (from index.html) -------------------------------
INK = "#181712"        # concrete-90, the ground
PALETTE = [
    "#4E9069",  # canopy-bright
    "#356B4D",  # canopy
    "#E36B54",  # coral
    "#EE9787",  # coral-soft
    "#3CA0AB",  # water
    "#7BC3CA",  # water-soft
    "#E0A552",  # amber
    "#F0C786",  # amber-soft
]

W, H = 1200, 520
SEED = 0x4B4F5A  # "KOZ"


def rng(state):
    """Tiny deterministic LCG -> float in [0, 1)."""
    while True:
        state = (1103515245 * state + 12345) & 0x7FFFFFFF
        yield state / 0x7FFFFFFF


def field_angle(x, y):
    """Smooth, swirling angle from a sum of sines — a free-flowing 'ki' field."""
    nx, ny = x / W, y / H
    a = math.sin(nx * 6.2 + math.cos(ny * 4.1) * 1.7)
    b = math.sin(ny * 5.3 - math.cos(nx * 3.4) * 1.3)
    c = math.sin((nx + ny) * 3.1)
    return (a + b + c) * 0.9 + math.pi * 0.15  # bias toward a rightward flow


def trace(x, y, steps=120, step=5.0):
    pts = [(x, y)]
    for _ in range(steps):
        ang = field_angle(x, y)
        x += math.cos(ang) * step
        y += math.sin(ang) * step
        if not (-40 <= x <= W + 40 and -40 <= y <= H + 40):
            break
        pts.append((x, y))
    return pts


def main():
    r = rng(SEED)
    streams = []
    n = 150
    for i in range(n):
        x = next(r) * W
        y = next(r) * H
        pts = trace(x, y)
        if len(pts) < 8:
            continue
        color = PALETTE[int(next(r) * len(PALETTE)) % len(PALETTE)]
        width = round(0.6 + next(r) * 2.4, 2)
        opacity = round(0.18 + next(r) * 0.42, 3)
        streams.append((pts, color, width, opacity))

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" '
        f'aria-label="Kozen Labs generative flow field — 浩然, the vast flowing spirit">',
        f'<rect width="{W}" height="{H}" fill="{INK}"/>',
        '<g fill="none" stroke-linecap="round">',
    ]
    for pts, color, width, opacity in streams:
        d = "M" + " L".join(f"{px:.0f},{py:.0f}" for px, py in pts)
        parts.append(
            f'<path d="{d}" stroke="{color}" stroke-width="{width}" '
            f'stroke-opacity="{opacity}"/>'
        )
    parts.append("</g>")
    # The mark, quiet, lower-right.
    parts.append(
        '<text x="1176" y="492" text-anchor="end" '
        'font-family="Space Mono, monospace" font-size="20" '
        'fill="#F6F3EC" fill-opacity="0.55" letter-spacing="2">浩然</text>'
    )
    parts.append("</svg>")

    out = "\n".join(parts) + "\n"
    with open("assets/kozen-generative.svg", "w") as f:
        f.write(out)
    print(f"wrote assets/kozen-generative.svg ({len(streams)} streams, {len(out)} bytes)")


if __name__ == "__main__":
    main()
