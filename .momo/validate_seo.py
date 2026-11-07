#!/usr/bin/env python3
"""Validate SEO elements across all HTML pages."""
import json
import re
import sys
from pathlib import Path


def validate_jsonld(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not matches:
        return False, "No JSON-LD found"
    try:
        json.loads(matches[0].strip())
        return True, "VALID"
    except json.JSONDecodeError as e:
        return False, f"INVALID JSON: {e}"


def validate_canonical(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    match = re.search(r'<link rel="canonical" href="([^"]+)">', content)
    return match is not None, match.group(1) if match else "MISSING"


def validate_og(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    required = ["og:type", "og:url", "og:title", "og:description", "og:image"]
    missing = []
    for prop in required:
        if f'property="{prop}"' not in content:
            missing.append(prop)
    return len(missing) == 0, missing


def validate_twitter(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    required = ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]
    missing = []
    for prop in required:
        if f'name="{prop}"' not in content:
            missing.append(prop)
    return len(missing) == 0, missing


def main():
    pages = [
        "index.html",
        "surrogate-model.html",
        "fault-tolerant.html",
        "ansys.html",
        "matlab.html",
        "momobot.html",
        "solidworks.html",
    ]
    
    all_ok = True
    print(f"{'File':<25} {'JSON-LD':<12} {'Canonical':<10} {'OG':<10} {'Twitter':<10}")
    print("-" * 70)
    
    for page in pages:
        if not Path(page).exists():
            print(f"{page:<25} {'MISSING':<12} {'MISSING':<10} {'MISSING':<10} {'MISSING':<10}")
            all_ok = False
            continue
            
        jsonld_ok, jsonld_msg = validate_jsonld(page)
        canonical_ok, canonical_url = validate_canonical(page)
        og_ok, og_missing = validate_og(page)
        twitter_ok, twitter_missing = validate_twitter(page)
        
        jsonld_status = "OK" if jsonld_ok else "FAIL"
        canonical_status = "OK" if canonical_ok else "FAIL"
        og_status = "OK" if og_ok else f"MISSING:{len(og_missing)}"
        twitter_status = "OK" if twitter_ok else f"MISSING:{len(twitter_missing)}"
        
        if not (jsonld_ok and canonical_ok and og_ok and twitter_ok):
            all_ok = False
            
        print(f"{page:<25} {jsonld_status:<12} {canonical_status:<10} {og_status:<10} {twitter_status:<10}")
        
        if not jsonld_ok:
            print(f"  -> JSON-LD: {jsonld_msg}")
        if not og_ok:
            print(f"  -> OG missing: {og_missing}")
        if not twitter_ok:
            print(f"  -> Twitter missing: {twitter_missing}")
    
    # Validate sitemap.xml
    print("\nSitemap validation:")
    try:
        import xml.etree.ElementTree as ET
        ET.parse("sitemap.xml")
        print("  sitemap.xml: VALID XML")
    except Exception as e:
        print(f"  sitemap.xml: INVALID - {e}")
        all_ok = False
    
    # Validate robots.txt
    print("\nRobots.txt validation:")
    robots = Path("robots.txt").read_text(encoding="utf-8")
    if "User-agent: *" in robots and "Sitemap:" in robots:
        print("  robots.txt: OK")
    else:
        print("  robots.txt: MISSING REQUIRED DIRECTIVES")
        all_ok = False
    
    print(f"\n{'ALL CHECKS PASSED' if all_ok else 'SOME CHECKS FAILED'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())