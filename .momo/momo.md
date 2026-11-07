# Project Overview
Personal portfolio website for Aniruddho Biswas Badhon — Computational Mechanical Engineer. Static HTML/CSS/JS site with 7 pages (index + 6 project pages). Hosted on GitHub Pages (inferred). Tech: Vanilla HTML5, CSS Custom Properties, IntersectionObserver animations, custom Anthropic fonts.

# Commands
- No build step — direct static deployment
- Local preview: `npx serve .` or `python -m http.server`
- Deploy: Push to `main` branch (GitHub Pages)

# Code Style & Conventions
- Semantic HTML5 with ARIA landmarks
- CSS Custom Properties for theming (--ink, --paper, --accent, etc.)
- Mobile-first responsive breakpoints: 600px, 900px, 1000px
- Fluid typography using `clamp()`
- BEM-adjacent class naming (.site-header, .project-list, .competency-card)
- Reduced-motion support via prefers-reduced-motion media query

# Architecture & Constraints
- **Single-page per project** pattern: index.html + 6 project pages (surrogate-model, fault-tolerant, ansys, matlab, momobot, solidworks)
- **Shared CSS/JS** across all pages (style.css, script.js)
- **Sidebar layout** on desktop (grid: 1fr 280px), stacked on mobile
- **Scroll-reveal animations** via IntersectionObserver (threshold: 0.08)
- **Custom fonts** self-hosted (AnthropicSerif, AnthropicSans, AnthropicMono) with font-display: swap
- **SVG diagrams** inline in HTML for technical illustrations
- **No framework, no build tool, no CMS**

# Mappings
- `/` (index.html) — Homepage / Portfolio index
- `/surrogate-model.html` — ML surrogate for FEA acceleration
- `/fault-tolerant.html` — ESP32 TMR self-healing firmware
- `/ansys.html` — ANSYS parametric automation pipeline
- `/matlab.html` — Signal processing, System ID, HIL
- `/momobot.html` — LangGraph/Ollama autonomous agent
- `/solidworks.html` — Parametric CAD, DriveWorks automation
- `/images/` — 3 JPG hero images (47KB, 47KB, 97KB)
- `/fonts/` — 3 Anthropic font families (TTF/Variable)
- `/surrogate-model/` — Project assets (SVG/PNG/CSV)

# Gotchas
- **Large images**: image_3.jpg is 97KB — no WebP/AVIF, no responsive srcset, no lazy loading
- **No SEO metadata**: Missing Open Graph, Twitter Cards, JSON-LD structured data, sitemap.xml, robots.txt
- **No analytics**: No GA4, no Search Console verification
- **No content marketing**: No blog, no RSS, no long-form technical articles for SEO
- **Mailto only**: No contact form, no newsletter capture
- **GitHub Pages limitations**: No server-side redirects, no custom headers, no dynamic features
- **Font loading**: 3 font families self-hosted — could benefit from preload hints
- **PDF certificates**: Large PDFs (354KB each) linked directly — no preview/thumbnails

# User Preferences
- Choice: Keep vanilla stack (no React/Next.js/Astro)
- Choice: Self-hosted fonts, custom design system
- To Do: Make Google-indexable, increase traffic, professional presence
- To Do: Connect with people (hiring, collaboration, speaking)
- Not To Do: Add framework complexity, lose design uniqueness, add bloat

# Memory
- Context: Strong technical content (6 detailed project pages with code, diagrams, metrics)
- Context: Unique niche — computational mechanics + embedded + local-first AI
- Context: High-quality writing with specific metrics (1.35M× speedup, 2.3ms inference, 47 Pareto solutions)
- Decisions: Current structure is project-centric, not blog-centric
- Learnings: Project pages are content-rich but lack structured data for rich snippets
- Learnings: Images unoptimized — major Core Web Vitals risk (LCP)

# Reasoning
> vanilla_stack : User values design control and zero-dependency simplicity
> project_pages : Each is a mini-case-study with code, diagrams, measurable outcomes
> seo_gap : Zero technical SEO implementation — invisible to search engines
> conversion_gap : No way to capture leads beyond mailto link
> performance_gap : Unoptimized images, no caching strategy, font loading not optimal

# Updates
- 2026-11-07: Initial audit complete. Identified 4 critical pillars for professional site: Technical SEO, Performance, Content Strategy, Conversion.
- 2026-11-07: Technical SEO complete (canonical, OG, Twitter, JSON-LD, sitemap, robots.txt). Pushed to main.

# Personal Brand & Business Development Plan
## Goal
Transform portfolio from passive showcase → active lead-generation engine for consulting/contracting/speaking in computational mechanics + embedded AI niche.

## Target Audiences (Priority Order)
1. **R&D Directors / Engineering Managers** at tech companies (automotive, aerospace, robotics, industrial IoT) — hiring for surrogate modeling, FEA automation, digital twin
2. **Startup CTOs / Founders** needing embedded AI, fault-tolerant systems, rapid prototyping
3. **Consulting Clients** with specific problems: simulation speedup, hardware reliability, design automation
4. **Conference Organizers / Podcast Hosts** seeking technical speakers on ML+Mechanics, local-first AI
5. **Recruiters / Hiring Managers** for senior/principal IC roles

## Unique Value Proposition (UVP)
"Computational mechanics engineer who replaces weeks of FEA with millisecond surrogates, builds aerospace-grade firmware that heals itself, and runs AI agents entirely on-premise. 1.35M× speedups. 99.999% fault coverage. Zero cloud dependency."

## 4-Pillar Execution Plan

### PILLAR 1: Authority Content (High Impact, Medium Effort)
**Strategy:** Publish 1 deep technical article/month targeting long-tail keywords. Repurpose into LinkedIn threads, newsletter, speaking abstracts.

| Content Piece | Target Keyword | Format | Lead Magnet |
|---------------|----------------|--------|-------------|
| "How I replaced 1,200 Ansys runs with a 2.3ms surrogate" | surrogate modeling FEA, ML for mechanical design | Case study + code | Jupyter notebook template |
| "TMR on ESP32: 99.999% fault coverage in <50ms recovery" | fault tolerant embedded systems, ESP32 reliability | Technical deep-dive | C++ TMR boilerplate |
| "Local-first AI agents: LangGraph + Ollama on-premise" | local LLM agents, on-premise AI, LangGraph tutorial | Tutorial + repo | Starter harness repo |
| "PyDPF pipeline: 500 sims in 2 min vs 45 min manual" | ANSYS automation, PyDPF, DesignXplorer | Walkthrough + script | Automation script pack |
| "Grey-box system ID for vibration: MathWorks certified workflow" | system identification MATLAB, grey box modeling | Methodology guide | Simulink template |

**Implementation:**
- Add `/writing/` section to site (static HTML pages, same stack)
- Each article: Problem → Method → Code → Results → Downloadable asset
- Capture email via "Get the code/template" form (Netlify Forms / Formspree / static form → Google Sheets via Apps Script)
- Cross-post to LinkedIn (primary), Twitter/X, Dev.to, Hacker News when relevant

### PILLAR 2: Conversion Architecture (High Impact, Low Effort)
**Current Gap:** Only `mailto:` — no capture, no qualification, no nurture.

**Add to every page:**
1. **Sticky CTA banner** (mobile) / **Sidebar CTA card** (desktop): "Need simulation speedup / fault-tolerant firmware / local AI? Book a 30-min technical discovery call."
2. **Inline lead magnets** per project page: "Download the surrogate modeling starter kit" → email gate
3. **Contact form** (Formspree/Netlify Forms → email + Google Sheet): Name, Email, Company, Project Type (Consulting/Contracting/Speaking/Hiring), Budget Range, Message
4. **Calendly/Cal.com embed** for direct booking (qualification questions built-in)
5. **Newsletter signup** (Buttondown/ConvertKit): "Monthly technical deep-dive — 2,000+ engineers read this"

**Static-site compatible stack:**
- Formspree (free tier: 50 submissions/mo) or Netlify Forms (if DNS moved)
- Calendly free tier + embed
- Buttondown (free tier: 1,000 subscribers) or Ghost (self-host later)

### PILLAR 3: Social Proof & Trust Signals (Medium Impact, Low Effort)
**Add to homepage sidebar / footer / project pages:**
- **Metrics bar**: "1.35M× FEA speedup • 99.999% fault coverage • 2.3ms inference • 47 Pareto designs • 500+ sims automated • 3 MathWorks certs"
- **Client/Employer logos** (anonymized if NDA): "Worked with teams at [Fortune 500 automotive] • [Robotics unicorn] • [Aerospace prime]"
- **Testimonials** (3-5): Request from former managers, collaborators, professors. Format: "Aniruddho reduced our simulation pipeline from weeks to hours..." — Name, Title, Company
- **Speaking/Podcasts**: List conferences, podcasts, webinars. Add "Available for speaking" badge.
- **GitHub stats**: Pinned repos with stars, commit activity badge (shields.io)
- **Certifications**: MathWorks badges, any AWS/Azure/GCP, safety standards (ISO 26262, DO-178C awareness)

### PILLAR 4: Service Positioning (High Impact, Low Effort)
**Create `/services.html` (or section on index) with 3 clear offerings:**

| Offering | Description | Ideal Client | Delivery |
|----------|-------------|--------------|----------|
| **Surrogate Modeling & FEA Acceleration** | Replace costly simulations with ML surrogates. PyDPF pipelines, design space exploration, Pareto optimization. | R&D teams running 100+ sims/week | 4-8 week engagement, code handoff |
| **Fault-Tolerant Embedded Systems** | TMR, SEU mitigation, flash recovery, watchdog architectures for ESP32/STM32/ARM. Aerospace/IoT/Industrial. | Hardware teams needing SIL/ASIL compliance | 6-12 week engagement, firmware + test suite |
| **Local-First AI Agent Development** | LangGraph/Ollama harnesses, tool chains, memory, on-premise reasoning. No cloud, no data egress. | Companies with IP/security constraints | 4-6 week engagement, production-ready harness |

**No public pricing.** Use "Start a conversation" → discovery call → custom proposal.

## Technical Implementation Roadmap

### Phase 1 (Week 1-2): Conversion Foundation
- [ ] Add Formspree contact form + Calendly embed to index.html + all project pages
- [ ] Add sticky CTA banner / sidebar card with "Book discovery call"
- [ ] Create `/services.html` with 3 offerings
- [ ] Add metrics bar to homepage hero
- [ ] Request 3 testimonials from past managers/collaborators

### Phase 2 (Week 3-4): Content Engine
- [ ] Build `/writing/` index page (list of articles)
- [ ] Publish Article 1: Surrogate modeling case study + code download (email gate)
- [ ] Set up Buttondown newsletter + embed signup forms
- [ ] Cross-post to LinkedIn (1 thread + 1 article republish/week)

### Phase 3 (Month 2): Authority Amplification
- [ ] Publish Article 2: TMR on ESP32
- [ ] Add client logos (anonymized) + speaking section
- [ ] Submit 3 conference CFPs / podcast pitches
- [ ] GitHub: Pin 3 best repos, add detailed READMEs with architecture diagrams

### Phase 4 (Month 3+): Scale
- [ ] Article 3: Local-first AI agents
- [ ] Article 4: ANSYS automation pipeline
- [ ] Launch "Technical Office Hours" monthly (Calendly, free 20-min, converts to paid)
- [ ] Consider moving to Cloudflare Pages + Workers for forms/analytics (still static)

## SEO Content Strategy (Topic Clusters)

**Pillar Page 1: "Surrogate Modeling for Mechanical Design"**
- Cluster: ML for FEA, Gaussian processes vs neural nets, active learning, design optimization
- Target: "surrogate model ansys", "FEA acceleration machine learning", "design space exploration python"

**Pillar Page 2: "Fault-Tolerant Embedded Firmware"**
- Cluster: TMR, watchdog design, flash corruption recovery, SEU mitigation, IEC 61508/ISO 26262
- Target: "ESP32 fault tolerance", "triple modular redundancy microcontroller", "self healing firmware"

**Pillar Page 3: "Local-First AI Agents"**
- Cluster: LangGraph, Ollama, on-premise LLMs, tool calling, memory architectures
- Target: "local AI agent framework", "langgraph ollama tutorial", "on premise llm agent"

**Pillar Page 4: "ANSYS Automation with Python"**
- Cluster: PyDPF, ACT extensions, DesignXplorer, parametric studies, HPC integration
- Target: "ansys python automation", "pydpf tutorial", "designxplorer scripting"

## Success Metrics (Track Monthly)
| Metric | Target (Month 3) | Target (Month 6) |
|--------|------------------|------------------|
| Organic sessions | 500/mo | 2,000/mo |
| Newsletter subscribers | 100 | 500 |
| Discovery calls booked | 5/mo | 15/mo |
| Proposals sent | 3/mo | 8/mo |
| Revenue (consulting/contracting) | $5k/mo | $20k/mo |
| Speaking invitations | 1/qtr | 1/mo |

## Constraints & Guardrails
- **Stay vanilla HTML/CSS/JS** — no framework, no build step
- **Static-compatible only** — Formspree, Calendly, Buttondown, Netlify Forms
- **No cookie banners** — use privacy-first tools (no GA4, use Cloudflare/Plausible if needed)
- **Preserve design uniqueness** — don't template-ize
- **One article/month max** — quality > quantity, repurpose heavily

## Next Immediate Action
1. Sign up for Formspree (free) → get form endpoint
2. Sign up for Calendly (free) → create "Technical Discovery Call" event type
3. Sign up for Buttondown (free) → get embed code
4. Draft services.html content
5. Email 3 past managers for testimonials (template provided)

---

*Reasoning:*
> content_first : Engineers trust technical depth — case studies with code beat marketing fluff
> static_constraints : GitHub Pages + vanilla stack means external services for forms/booking
> niche_authority : Computational mechanics + embedded + local AI is rare — own the intersection
> consultation_model : High-ticket, low-volume — discovery call qualifies, proposal closes
> newsletter_compound : Email list = owned audience, survives algorithm changes

# Entity Optimization & Knowledge Graph Strategy (AI/Search Visibility)
## Goal
Make "Aniruddho Biswas Badhon" a recognized entity in Google Knowledge Graph, Bing, and LLM training data so queries for the name return this website as the authoritative source.

## Technical Implementation (Deploy This Week)

### 1. JSON-LD Person Schema (index.html)
Add to homepage `<head>` — defines the entity with `sameAs` linking all profiles:
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Aniruddho Biswas Badhon",
  "url": "https://aniruddh5502.github.io/",
  "image": "https://aniruddh5502.github.io/images/hero-portrait.jpg",
  "jobTitle": "Computational Mechanical Engineer",
  "worksFor": {"@type": "Organization", "name": "Self-Employed / Consulting"},
  "knowsAbout": ["Surrogate Modeling", "FEA Automation", "Fault-Tolerant Embedded Systems", "Local-First AI Agents", "ANSYS", "MATLAB", "SOLIDWORKS", "Python", "C++", "LangGraph", "Ollama"],
  "sameAs": [
    "https://github.com/Aniruddh5502",
    "https://linkedin.com/in/aniruddh5502",
    "https://scholar.google.com/citations?user=...",
    "https://orcid.org/...",
    "https://twitter.com/aniruddh5502"
  ],
  "description": "Computational mechanics engineer specializing in ML surrogates for FEA acceleration (1.35M× speedup), fault-tolerant embedded firmware (99.999% coverage), and local-first AI agent systems."
}
```

### 2. llms.txt (New Standard for AI Crawlers)
Create `/llms.txt` at root — tells AI agents what the site is about:
```
# Aniruddho Biswas Badhon — Computational Mechanical Engineer
> Portfolio and technical blog for Aniruddho Biswas Badhon, specializing in surrogate modeling for FEA acceleration, fault-tolerant embedded systems, and local-first AI agents.

## Key Pages
- [Homepage](https://aniruddh5502.github.io/) — Overview of expertise and projects
- [Surrogate Model Framework](https://aniruddh5502.github.io/surrogate-model.html) — 1.35M× FEA speedup via ML surrogates
- [Fault-Tolerant ESP32 Firmware](https://aniruddh5502.github.io/fault-tolerant.html) — TMR with 99.999% fault coverage
- [ANSYS Automation](https://aniruddh5502.github.io/ansys.html) — 500+ simulations automated via PyDPF
- [MATLAB Signal Processing & System ID](https://aniruddh5502.github.io/matlab.html) — MathWorks certified workflows
- [Momobot: Local-First AI Agent](https://aniruddh5502.github.io/momobot.html) — LangGraph + Ollama harness
- [SOLIDWORKS Automation](https://aniruddh5502.github.io/solidworks.html) — Parametric CAD & API-driven design

## Author
Aniruddho Biswas Badhon — Computational Mechanical Engineer
- GitHub: https://github.com/Aniruddh5502
- LinkedIn: https://linkedin.com/in/aniruddh5502
```

### 3. robots.txt — Allow AI Crawlers
Update to explicitly allow major AI bots:
```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: https://aniruddh5502.github.io/sitemap.xml
```

### 4. WebSite + Organization Schema (index.html)
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "url": "https://aniruddh5502.github.io/",
  "name": "Aniruddho Biswas Badhon — Computational Mechanical Engineer",
  "author": {"@type": "Person", "name": "Aniruddho Biswas Badhon"},
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://aniruddh5502.github.io/?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

## External Entity Signals (Ongoing)

| Platform | Action | Why |
|----------|--------|-----|
| **GitHub** | Pin 3 best repos, detailed READMEs, link to site in bio | High-authority signal, code proof |
| **LinkedIn** | Custom URL, detailed experience matching site projects, link to site | Professional graph, recruiter search |
| **Google Scholar** | Claim profile, link publications to site pages | Academic authority |
| **ORCID** | Create ID, add works, link to site | Persistent researcher identifier |
| **Wikidata** | Create Q-item (easier than Wikipedia) | Feeds Google Knowledge Graph directly |
| **ResearchGate** | Profile with publications linking to site | Academic network |
| **Guest Content** | Podcasts, conference talks, guest articles with author bio linking to site | Third-party validation |

## Verification Checklist
- [ ] Person JSON-LD on index.html (validate with Rich Results Test)
- [ ] llms.txt at root (check: `curl https://aniruddh5502.github.io/llms.txt`)
- [ ] robots.txt allows AI bots
- [ ] WebSite schema on index.html
- [ ] Google Search Console: verify ownership, submit sitemap.xml
- [ ] Bing Webmaster Tools: submit sitemap
- [ ] All social profiles use **exact same name**: "Aniruddho Biswas Badhon"
- [ ] All profiles link to `https://aniruddh5502.github.io/`
- [ ] Request Wikidata entry (via WikiData Request a new item)

## Why This Works
- **Consistent entity name** across all properties = knowledge graph reconciliation
- **sameAs** links create a "hub" — Google/Bing/LLMs crawl these and associate them
- **llms.txt** is the emerging standard (adopted by Anthropic, OpenAI, others) for AI crawler guidance
- **Person + WebSite schema** makes the site the "official" home page for the entity
- **Wikidata** is the structured backend for Google Knowledge Panels

---

*Reasoning:*
> entity_first : LLMs and search engines reconcile entities via consistent identifiers across sources
> llms_txt : New standard (2024) — early adoption puts site in training/augmentation pipelines
> wikidata : Single source of truth for Knowledge Graph; easier than Wikipedia notability
> schema_person : Explicitly tells crawlers "this is the person, these are their properties"
> cross_link : Bidirectional links (site→profiles, profiles→site) = trust signal