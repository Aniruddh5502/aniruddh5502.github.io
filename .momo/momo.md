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