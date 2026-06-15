<div align="center">

![Kozen Labs — generative flow field](assets/kozen-generative.svg)

# Kozen Labs

**Consultora boutique de IA — estrategia, ingeniería, diseño e IA en un solo equipo senior.**

</div>

---

## 浩然 — the meaning

The art above is generated from the idea behind the name. **Kōzen (浩然)** comes from
classical Chinese and Japanese thought: *kōzen no ki* (浩然の気), the **"vast, flowing
vital spirit"** described by Mencius — a boundless, free-flowing moral energy that is
disciplined yet expansive.

That is the brief the artwork renders. Each line is an independent stream threading a
single flow field: many currents, distinct in colour and weight, all moving as one. It
is drawn algorithmically from the project's own design tokens — concrete, canopy, coral,
water and amber — the same palette that drives the site.

## The site

A single-page static site for Kozen Labs, a matrix-style boutique consultancy. From
architecture to launch, no dilution.

```
.
├── index.html        # the entire site (self-contained: styles + markup)
├── assets/
│   ├── kozen-mark.svg          # brand mark
│   ├── kozen-mark-inverse.svg  # brand mark, inverse
│   └── kozen-generative.svg    # generated art (see below)
└── tools/
    └── generate_art.py         # generative-art renderer
```

## The generative art

The header image is **algorithmic art**, not a static asset drawn by hand. It is a
flow-field traced by [`tools/generate_art.py`](tools/generate_art.py):

- A smooth field of swirling angles is built from a sum of sines — a stand-in for the
  free-flowing *ki*.
- Hundreds of particles are seeded across the canvas and traced as they follow the
  field, each becoming one stream.
- Colour, weight and opacity are sampled from the Kozen palette.

It is **deterministic** — a fixed seed and no external dependencies — so the committed
SVG is fully reproducible. To regenerate:

```bash
python3 tools/generate_art.py
```

Tune `SEED`, `n`, and the `field_angle` coefficients to explore other compositions.

## Develop

The site is fully static — open it directly or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy

Deployed on Vercel (`.vercel` is local and git-ignored).

---

<div align="center">
<sub>浩然 — vast, flowing, undiluted.</sub>
</div>
