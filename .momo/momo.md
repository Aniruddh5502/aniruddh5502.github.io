# Project Overview
Personal portfolio for Aniruddho Biswas Badhon — Computational Mechanical Engineer. Static vanilla HTML/CSS/JS (7 pages). GitHub Pages. Self-hosted Anthropic fonts. No framework, no build.

# Commands
- Preview: `npx serve .` or `python -m http.server`
- Deploy: Push to `main`

# Stack & Conventions
- Semantic HTML5, CSS Custom Properties, fluid `clamp()` typography
- Breakpoints: 600px, 900px, 1000px | Sidebar grid (1fr 280px) → stacked mobile
- IntersectionObserver scroll-reveal (threshold: 0.08)
- BEM-adjacent classes | Reduced-motion support

# Pages
| Path | Topic |
|------|-------|
| `index.html` | Portfolio index |
| `surrogate-model.html` | ML surrogate for FEA (1.35M× speedup) |
| `fault-tolerant.html` | ESP32 TMR firmware (99.999% coverage) |
| `ansys.html` | PyDPF automation (500+ sims) |
| `matlab.html` | Signal processing, System ID, HIL |
| `momobot.html` | LangGraph/Ollama local agent |
| `solidworks.html` | Parametric CAD, DriveWorks |

# Assets
- `/images/` — 3 JPGs (47KB, 47KB, 97KB) — unoptimized
- `/fonts/` — 3 Anthropic families (TTF/Variable)
- `/surrogate-model/` — Project assets

# Done (Technical SEO + Entity Foundation)
- ✅ Canonical, OG, Twitter Cards on all pages
- ✅ `SoftwareApplication` JSON-LD on 6 project pages
- ✅ `Person` + `WebSite` JSON-LD on homepage
- ✅ `robots.txt` allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended
- ✅ `llms.txt` at root
- ✅ `sitemap.xml` submitted to GSC + Bing
- ✅ Social profiles unified: "Aniruddho Biswas Badhon" → site URL

# Remaining Tasks (AEO/GEO + Conversion)

## Entity & Authority
- [ ] **Wikidata Q-item**: Create at wikidata.org (P31:Q5, P106:Q42973, P856, P2013, P6634, P496)
- [ ] **ORCID + Google Scholar**: Claim profiles, link to site
- [ ] **GitHub**: Pin 3 repos, detailed READMEs with problem→method→metrics→site link

## Structured Data (High ROI for Answer Engines)
- [ ] **FAQPage JSON-LD + visible `<details>` Q&A** on all 6 project pages (3–5 Qs each)
- [ ] **HowTo JSON-LD** on ANSYS, MATLAB, SOLIDWORKS pages (methodology pipelines)

## Conversion & Content
- [ ] **Services page** (`/services.html`): 3 offerings + Formspree form + Calendly embed
- [ ] **Homepage metrics bar**: 6 key numbers (1.35M×, 99.999%, 2.3ms, 47, 500+, 40×)
- [ ] **Writing section** (`/writing/`): Article 1 (surrogate case study) + Buttondown newsletter
- [ ] **Key Answers sections**: Rewrite project page bodies as explicit Q&A blocks

## Constraints
- Vanilla HTML/CSS/JS only — no framework, no build
- Static-compatible services only (Formspree, Calendly, Buttondown)
- No cookie banners — privacy-first
- Preserve design uniqueness

---

*Reasoning:*
> entity_first : Consistent identifiers across sources = Knowledge Graph reconciliation
> faq_howto : FAQPage + HowTo schema = direct answer extraction by AI agents
> static_stack : GitHub Pages + vanilla = external services for forms/booking
> niche_authority : Computational mechanics + embedded + local AI = own the intersection