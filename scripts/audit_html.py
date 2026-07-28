#!/usr/bin/env python3
"""Offline blocking audit for WeChat article HTML."""
from __future__ import annotations
import json,re,sys
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
BAD_CSS=re.compile(r"position\s*:\s*(?:fixed|sticky)|@import|display\s*:\s*none",re.I)
BAD_TAG=re.compile(r"<(?:script|iframe|form|input|button)\b",re.I)
SENSITIVE=re.compile(r"(?:\b[A-Za-z]:[\\/]|/(?:Users|home|var|tmp)/|sk-[A-Za-z0-9_-]{12,}|-----BEGIN|Bearer\s+[A-Za-z0-9._-]{12,})",re.I)
class Scanner(HTMLParser):
    def __init__(self): super().__init__(); self.sources=[]; self.takeaway=False; self.connect=False
    def handle_starttag(self,tag,attrs):
        data=dict(attrs)
        if tag=="img": self.sources.append(data.get("src", ""))
        classes=data.get("class","").split()
        if "takeaway" in classes: self.takeaway=True
        if "connect" in classes: self.connect=True
def inspect(html):
    parser=Scanner(); parser.feed(html)
    return {"html_present":bool(re.search(r"<article\b|<body\b",html,re.I) and re.search(r"<h1\b",html,re.I)),"forbidden_css":not bool(BAD_CSS.search(html) or BAD_TAG.search(html)),"image_hosts":not bool(parser.sources) or all(src.startswith("https://mmbiz.qpic.cn/") for src in parser.sources),"takeaway":parser.takeaway,"connect_present":parser.connect,"sensitive_content":not bool(SENSITIVE.search(html))}
def main():
    if len(sys.argv)!=2: print("Usage: audit_html.py ARTICLE.html",file=sys.stderr); return 2
    try: html=Path(sys.argv[1]).read_text(encoding="utf-8")
    except OSError as exc: print(f"AUDIT ERROR: {exc}"); return 2
    checks=json.loads((ROOT/"references/audit-checklist.yaml").read_text(encoding="utf-8"))["checks"]
    result=inspect(html); passed=0; print(f"AUDIT TOTAL: {len(checks)}")
    for check in checks:
        ok=result.get(check["id"],False); passed+=ok; print(f"{'PASS' if ok else 'FAIL'} {check['id']}: {check['label']}")
    print(f"AUDIT {'PASS' if passed==len(checks) else 'FAIL'}: {passed}/{len(checks)}")
    return 0 if passed==len(checks) else 1
if __name__=="__main__": raise SystemExit(main())
