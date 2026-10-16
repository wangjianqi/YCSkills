---
name: appstore-creative-assets
description: >
  Create minimalist, premium, brand-consistent App Store creative assets for Apple's
  Product Page Header and Search Results placements. First analyze the target app's
  visual identity, UI, product positioning, and strongest value proposition; then
  generate placement-specific compositions at Apple's supported aspect ratios and
  resolutions. Use the app's actual visual language rather than generic marketing
  templates. Apply concise copy, controlled composition, localization-aware typography,
  and Apple marketing-asset constraints. Use this skill whenever a user asks to create,
  redesign, or adapt App Store Product Page Header or Search Results image assets.
---

# App Store Creative Assets

## 1. Purpose

This skill creates production-oriented visual concepts and generation prompts for:

- **Product Page Header**
- **Search Results**

The skill is intentionally **app-agnostic**.

Do not assume that every app should be:

- black and white
- futuristic
- glassmorphic
- 3D
- gradient-heavy
- device-mockup based
- "luxury"

The app's actual visual identity is the source of truth.

### Core principle

> **Understand the app first. Communicate one idea clearly. Decorate only when decoration has a purpose.**

The output should feel like an extension of the product, not a generic AI advertisement.

---

# 2. Scope

## Supported placements

### Product Page Header

- 21:9 — **3840 × 1646 px**
- 16:9 — **5244 × 2950 px**

### Search Results

- 3:2 — **1920 × 1280 px minimum**
- 3:2 — **3840 × 2560 px maximum**
- 16:9 — **5244 × 2950 px**

Images must not contain an alpha channel or transparency.

For the 3:2 Search Results format, prefer the maximum supported resolution when the generation workflow can reliably produce it.

> Apple specifications are external requirements and may change. The bundled reference records the specification checked for this skill version; verify Apple's current documentation before final submission.

See `references/apple-specifications.md`.

---

# 3. Input hierarchy

Use information in this priority order:

1. **User-provided screenshots**
2. **User-provided app icon / logo**
3. **User-provided existing App Store assets**
4. **User-provided product website / brand guide**
5. **User-provided product description**
6. **Careful visual inference**

If multiple sources conflict, prefer the newest explicit user-provided reference.

Do not invent visual details that can be observed directly.

---

# 4. Mandatory workflow

Never jump directly from "app name + feature list" to a generic marketing composition when visual references are available.

Follow this pipeline:

```text
INPUT
  ↓
Reference inspection
  ↓
Product understanding
  ↓
Visual DNA extraction
  ↓
Message selection
  ↓
Copy direction
  ↓
Placement strategy
  ↓
Composition
  ↓
Generation / editing
  ↓
Technical QA
  ↓
Brand QA
  ↓
Apple marketing QA
  ↓
Final asset family
```

---

# 5. Phase A — Understand the product

Extract only information that materially affects the creative.

## Product profile

Determine:

- App name
- Product category
- Primary use case
- Target audience, if supplied
- Core differentiator
- Most visually demonstrable capability
- Most important conversion message
- Platform / device context, if relevant

Do not turn the creative into a feature list.

### Message priority

Rank candidate messages:

1. Core product value
2. Strongest visual transformation
3. Most differentiating capability
4. Secondary capability
5. Supporting detail

Use one primary message per asset.

---

# 6. Phase B — Extract the app's Visual DNA

Build an internal visual profile before designing.

## Required dimensions

### Color

Identify:

- background color
- surface colors
- text contrast
- accent colors
- gradient usage
- saturation level

### Typography

Identify:

- serif / sans / display / monospaced character
- weight
- capitalization
- letter spacing
- headline density
- alignment

Do not invent a font family if the reference does not establish one.

### Shape language

Identify:

- corner radius
- card geometry
- line weight
- button shape
- icon geometry
- border treatment

### Material language

Identify whether the product uses:

- flat surfaces
- translucency
- glass
- blur
- metallic surfaces
- shadows
- soft elevation
- hard edges
- paper / editorial texture
- photographic depth

### Image language

Identify whether the product relies on:

- UI screenshots
- photography
- illustration
- 3D
- charts
- diagrams
- typography
- animation
- product imagery

### Density

Classify the interface as:

- extremely sparse
- sparse
- balanced
- dense
- information-dense

Do not create a sparse marketing composition for an app whose identity depends on dense data unless the product message still remains recognizable.

---

# 7. Visual DNA output

Internally reduce the analysis to a compact design system:

```text
VISUAL DNA

Background:
Surface:
Primary text:
Secondary text:
Accent:
Typography:
Geometry:
Material:
Depth:
Image language:
Density:
Brand personality:
Do / Don't:
```

The most important rule:

> **Marketing material may amplify an existing visual language, but should not replace it with a new one.**

If the app is already highly distinctive, preserve that identity.

If the app is visually inconsistent, use the strongest recurring patterns rather than inventing a completely new brand system.

---

# 8. Phase C — Choose the visual concept

Before generating, choose a concept based on the product.

Prefer these concept types:

### 1. Product-first

Show the actual app UI or product output.

Best for:

- utilities
- productivity apps
- editors
- professional tools
- developer tools

### 2. Transformation

Show the "before → after" or input → result relationship.

Best for:

- editors
- converters
- AI tools
- scanners
- photo/video tools

### 3. Capability

Show one distinctive feature in a highly recognizable state.

Best for:

- creative tools
- specialized utilities
- technical apps

### 4. Workflow

Show a compact visual sequence of a key task.

Best for:

- complex productivity tools
- professional workflows
- creation tools

### 5. Brand statement

Use the app name, a concise proposition, and one strong product visual.

Best for:

- launch assets
- premium products
- apps with a strong existing identity

Do not use abstract "AI-looking" imagery merely because the app contains AI.

---

# 9. Phase D — Write the copy

## Default hierarchy

```text
APP NAME

Short benefit headline

Optional supporting line
```

The app name is optional in the visual composition when the product identity is already obvious, but it is useful when establishing brand recognition.

## Headline rules

Prefer:

- short
- concrete
- benefit-led
- visually scannable
- natural language

Avoid:

- keyword stuffing
- long feature lists
- unsupported superlatives
- fake rankings
- fake awards
- fake review counts
- fake user counts
- unsupported performance claims
- excessive punctuation
- "AI-powered" unless materially relevant and supported
- vague claims such as "The future is here"

### Good pattern

```text
Create polished documents.
```

### Weak pattern

```text
The Ultimate AI-Powered Revolutionary Document Experience
```

The first communicates. The second looks like advertising filler.

---

# 10. App name treatment

When the user asks to use the app name:

- preserve the exact official app name
- respect capitalization
- do not add fake suffixes
- do not turn the name into a logo unless a logo reference exists
- do not distort the app icon
- do not replace the app name with a generic category label

If the app name is visually long, use typography and hierarchy rather than shrinking it until unreadable.

---

# 11. Placement strategy

The same campaign should feel like one family, but each placement must be composed independently.

## Product Page Header — 21:9

Use the width to establish a strong visual relationship.

Good structures:

```text
[brand + message]                 [product visual]
```

```text
[product visual]                  [brand + message]
```

```text
[large product visual spanning center]
             [small copy]
```

Use generous horizontal negative space.

Do not put essential information at the extreme edges.

Avoid compositions that depend on tiny UI details.

---

## Product Page Header — 16:9

This is a broader landscape composition.

Possible structures:

```text
[copy]                  [hero product]
```

```text
             [headline]
          [hero product]
```

```text
[large visual]          [compact copy]
```

Choose based on the app's visual DNA.

Do not mechanically crop a 21:9 design.

---

## Search Results — 3:2

This is a high-density discovery placement.

Prioritize:

1. recognizable product
2. app identity
3. one clear message

Use less copy than the Product Page Header.

The visual should remain recognizable when the asset is displayed substantially smaller than its source resolution.

---

## Search Results — 16:9

Treat it as an independent landscape composition that shares the same campaign system.

Do not stretch the 3:2 version.

---

# 12. Composition rules

## Default

Use:

- one focal point
- clear hierarchy
- intentional negative space
- consistent alignment
- restrained typography
- controlled depth
- product-led imagery

## Element budget

Start with:

- 1 app/product visual
- 1 app name
- 1 headline
- 0–1 supporting line
- 0–1 subtle environmental element

Only add more if the product meaning genuinely improves.

## Remove-first test

Before finalizing, ask:

- Can an element be removed without losing meaning?
- Can the headline be shortened?
- Can the supporting line disappear?
- Is the app still recognizable?
- Is there one obvious focal point?
- Is the background competing with the product?
- Does the composition still work as a small thumbnail?

If yes, remove it.

---

# 13. UI screenshot rules

When actual app screenshots are supplied:

## Preserve

- real UI
- real content
- real interaction states
- real iconography
- actual hierarchy
- important visual behavior

## Allowed presentation treatments

- strategic cropping
- masking
- layering
- controlled perspective when appropriate
- subtle shadow
- restrained scaling
- partial UI framing

## Avoid

- rewriting UI text without permission
- inventing screens
- replacing the UI with a fake interface
- shrinking the entire UI until it becomes unreadable
- changing critical states
- introducing visual components that do not exist in the app

The screenshot is product evidence, not merely decorative texture.

---

# 14. Device imagery and Apple products

This section is intentionally conservative.

Apple's current marketing guidelines state that Apple-provided product bezels should be used in marketing materials when displaying apps on Apple devices, and that Apple product images must be used as provided. The guidelines prohibit rendering or creating 3D simulations of Apple products for marketing materials.

Therefore:

- Prefer Apple's current approved product imagery / bezels when an Apple device must be shown.
- Do not invent a photorealistic 3D iPhone, iPad, Mac, Apple Watch, or other Apple product for marketing use.
- Do not modify Apple-provided product images in prohibited ways.
- Do not place competing-device product imagery beside Apple product imagery.
- Generic device illustrations may be used only when they do not imitate Apple-specific hardware details.
- Do not imply Apple endorsement or partnership.

If the app itself creates 3D device mockups, distinguish **the app's functionality** from **the marketing representation of an Apple product**. Showing a screenshot of the app's UI can communicate the functionality without fabricating an Apple product render.

Always re-check Apple's current guidelines before publication.

See `references/apple-marketing-guidelines.md`.

---

# 15. App icon and logo

If an icon is supplied:

- preserve its geometry
- preserve its colors
- preserve its proportions
- use it as a brand anchor when useful

Do not:

- redesign it automatically
- add arbitrary 3D extrusion
- add bevels
- add glow
- turn it into a metallic object
- place it in a giant decorative badge

A simple icon can be more effective when given enough negative space.

---

# 16. Localization

Generate localized compositions separately.

Do not treat localization as a simple text replacement.

Check:

- headline width
- line breaks
- punctuation
- font fallback
- character density
- optical alignment
- vertical rhythm
- balance between copy and product
- whether the app name changes by locale

### Simplified Chinese

Prefer:

- compact hierarchy
- clean Chinese typography
- controlled line breaks
- no excessive tracking
- sufficient character size

Do not force English line lengths onto Chinese copy.

### English

Prefer:

- concise headlines
- natural title/sentence case based on the app's identity
- readable line length

Other locales should follow the same principle.

---

# 17. Asset family strategy

When multiple assets are requested for one app, build a family.

Keep constant:

- visual DNA
- typography system
- color system
- material language
- spacing logic
- product rendering approach
- copy tone

Vary:

- focal visual
- composition
- feature
- crop
- message

Example:

```text
Asset 01 — Core proposition
Asset 02 — Key capability
Asset 03 — Transformation
Asset 04 — Advanced workflow
```

Do not make every asset identical.

Do not make every asset completely different.

The goal is:

> **recognizable as one brand, useful as separate messages.**

---

# 18. Generation prompt construction

When using an image-generation model, construct the prompt from evidence.

Use this order:

```text
1. Placement
2. Exact aspect ratio
3. App name
4. Product category
5. Primary message
6. Visual DNA
7. Actual reference assets
8. Focal visual
9. Composition
10. Typography hierarchy
11. Lighting/material
12. Negative space
13. Restrictions
```

## Generic prompt template

```text
Create a premium App Store creative asset for [APP NAME].

Placement: [PRODUCT PAGE HEADER / SEARCH RESULTS]
Aspect ratio: [21:9 / 16:9 / 3:2]

Product:
[ONE-SENTENCE PRODUCT DESCRIPTION]

Primary message:
[SHORT BENEFIT]

Visual identity:
[VISUAL DNA]

Use the supplied app screenshots / icon as the primary visual reference.
Preserve the app's actual visual language, UI hierarchy, typography character,
color relationships, geometry, and material treatment.

Composition:
[DESCRIBE THE SINGLE FOCAL POINT AND LAYOUT]

Typography:
[APP NAME + SHORT HEADLINE + OPTIONAL SUPPORTING LINE]

Keep the design minimal, restrained, precise, product-led, and highly legible.
Use negative space intentionally.

Do not introduce unrelated visual styles.
Do not add decorative elements without a communication purpose.
Do not invent product capabilities, claims, statistics, awards, ratings, or users.
Do not create fake app UI.
Do not distort supplied screenshots.
Do not create unauthorized Apple product simulations.
```

The actual generation prompt should replace placeholders with evidence from the app.

---

# 19. Generation vs. post-processing

Prefer a two-stage workflow when tooling allows:

### Stage 1 — Creative generation

Generate the composition and visual hierarchy.

### Stage 2 — Precision finishing

Use a deterministic graphics tool for:

- exact resolution
- exact text
- final typography
- alignment
- safe margins
- localization
- alpha-channel removal
- format conversion

This is preferable to relying on image generation for small, exact text.

If the image model reliably handles the required text, it may be used, but final QA remains mandatory.

---

# 20. Technical QA

Before declaring an asset production-ready:

### Dimensions

Verify exact output dimensions for the requested placement.

### Aspect ratio

Verify mathematically, not visually.

### Color / transparency

Verify that the image does not contain an alpha channel or transparency.

### Content

Check for:

- malformed text
- misspellings
- distorted UI
- broken icons
- duplicated elements
- impossible geometry
- unintended artifacts
- clipped headlines
- accidental watermarks
- unexpected logos

### Legibility

Check at:

1. 100% source resolution
2. approximately App Store display size
3. thumbnail-like size

An asset that only works at 100% zoom is not successful.

---

# 21. Brand QA

Ask:

```text
Does this look like the app?
Does it use the app's visual DNA?
Is the product itself the hero?
Is the background subordinate?
Is the design minimal without becoming empty?
Is there one clear message?
Would a user recognize the app from the visual alone?
```

If the answer to several is "no", redesign rather than adding more decoration.

---

# 22. Apple marketing QA

Before final delivery:

- Confirm the placement and dimensions against Apple's current creative-asset specification.
- Confirm no alpha / transparency.
- Confirm Apple product imagery follows current Apple marketing guidelines.
- Do not imply Apple endorsement.
- Do not fabricate Apple product simulations.
- Do not make unsupported claims.
- Use correct Apple product names when they appear in copy.
- Keep the marketing message focused on the app.

Apple requirements can change. The official documentation is authoritative.

---

# 23. What to do with insufficient references

Do not ask for a full design brief by default.

If the user supplies enough information to make a conservative concept:

- proceed
- use typography and layout as primary design tools
- avoid inventing complex visual effects

Ask for more information only when the missing reference would materially change the visual direction.

High-value missing references include:

- a representative app screenshot
- app icon
- existing App Store screenshots
- brand guideline
- website
- exact app name

---

# 24. Default behavior

Unless the user specifies otherwise:

- Generate **one strongest concept first**.
- Use the app's existing visual identity as the source of truth.
- Prefer minimal over decorative.
- Prefer real UI over fake UI.
- Prefer one focal point.
- Prefer concise copy.
- Prefer independent placement-specific compositions.
- Prefer consistent asset families.
- Use the exact Apple-supported dimensions requested.
- Treat technical QA as part of the design task, not an optional afterthought.

Do not produce a generic "AI marketing poster".

---

# 25. Deliverable format

When the user asks for a complete asset set, organize the result as:

```text
App Store Creative Assets
├── Product Page Header
│   ├── 21x9
│   └── 16x9
└── Search Results
    ├── 3x2
    └── 16x9
```

For each generated asset, identify:

- placement
- aspect ratio
- resolution
- language
- primary message
- concept

If the tool cannot directly produce exact production resolution, explicitly distinguish:

- generated concept
- production-resolution finishing required

Never claim exact technical compliance without verification.

---

# 26. Failure modes to avoid

### Generic template syndrome

**Bad:** Every app gets a dark gradient, glowing device, and giant text.

**Correct:** Derive the visual system from the actual app.

### Over-design

**Bad:** Add particles, 3D objects, gradients, reflections, and floating UI.

**Correct:** Add only elements that communicate the product.

### Screenshot collage

**Bad:** Put six tiny screenshots into one image.

**Correct:** Select one strong state or one coherent visual sequence.

### Copy overload

**Bad:** Feature list disguised as marketing copy.

**Correct:** One message.

### Brand drift

**Bad:** App is minimal but the marketing asset becomes colorful and futuristic.

**Correct:** Amplify the existing identity.

### AI artifact acceptance

**Bad:** Accept malformed text or distorted UI because the overall image looks good.

**Correct:** Treat exact UI and text as production content and QA them.

### Placement stretching

**Bad:** Stretch one artwork across 21:9, 16:9, and 3:2.

**Correct:** Recompose each placement while preserving the campaign system.

### Unsupported Apple device simulation

**Bad:** Generate a photorealistic 3D iPhone for marketing.

**Correct:** Use Apple's approved product imagery where applicable, or communicate the product through actual app UI / compliant generic-device treatment.

---

# 27. Quick decision tree

```text
Does the user provide screenshots?
  ├─ Yes → inspect screenshots first
  └─ No → use supplied brand/product references

Is the app visually distinctive?
  ├─ Yes → preserve and amplify it
  └─ No → create a restrained system from recurring patterns

Is there one obvious product benefit?
  ├─ Yes → use it
  └─ No → choose the most visually demonstrable differentiator

Does the placement change?
  ├─ Yes → recompose
  └─ No → preserve composition

Is exact text important?
  ├─ Yes → prefer deterministic post-processing
  └─ No → image generation may handle it

Is an Apple product shown?
  ├─ Yes → follow current Apple marketing guidelines
  └─ No → normal product-visual rules

Does the asset still work as a thumbnail?
  ├─ Yes → continue QA
  └─ No → simplify
```

---

# 28. Quality bar

The target is not:

> "This looks like a nice AI-generated image."

The target is:

> **"This looks like the product's own professional App Store marketing material."**

A successful asset is:

- recognizable
- restrained
- product-led
- visually coherent
- legible
- technically correct
- localization-aware
- compliant with current Apple marketing requirements
- consistent with the rest of the app's App Store presence
