#!/usr/bin/env python3
"""Validate a local workflow profile without third-party dependencies."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
FORBIDDEN_KEY=re.compile(r"(?:secret|token|password|credential|api[_-]?key|client[_-]?key)",re.I)
FORBIDDEN_VALUE=re.compile(r"(?:sk-[A-Za-z0-9_-]{12,}|-----BEGIN|Bearer\s+[A-Za-z0-9._-]{12,})",re.I)
ABS_PATH=re.compile(r"(?:\b[A-Za-z]:[\\/]|/(?:Users|home|var|tmp)/)")
REQUIRED={"brand":("name","tagline","voice","avoid"),"audience":("primary","needs"),"visual":("accent_color","image_style","approved_image_hosts"),"connection":("primary_channel","account_name","invitation"),"monetization":("offers","claims_policy"),"publishing":("mode","requires_explicit_confirmation")}
def walk(value,trail="$"):
    if isinstance(value,dict):
        for key,item in value.items():
            if FORBIDDEN_KEY.search(key): yield f"{trail}.{key}: credential-like key is not allowed in profiles"
            yield from walk(item,f"{trail}.{key}")
    elif isinstance(value,list):
        for i,item in enumerate(value): yield from walk(item,f"{trail}[{i}]")
    elif isinstance(value,str):
        if FORBIDDEN_VALUE.search(value): yield f"{trail}: credential-like value detected"
        if ABS_PATH.search(value): yield f"{trail}: absolute local path detected"
def validate(profile):
    errors=[]
    if not isinstance(profile,dict): return ["profile must be a JSON object"]
    if profile.get("schema_version") != 1: errors.append("schema_version must be 1")
    for section,fields in REQUIRED.items():
        item=profile.get(section)
        if not isinstance(item,dict): errors.append(f"missing object: {section}"); continue
        for field in fields:
            if item.get(field) in (None,"",[]): errors.append(f"missing value: {section}.{field}")
    if profile.get("publishing",{}).get("requires_explicit_confirmation") is not True: errors.append("publishing.requires_explicit_confirmation must be true")
    errors.extend(walk(profile)); return errors
def main():
    if len(sys.argv)!=2: print("Usage: validate_profile.py PROFILE.json",file=sys.stderr); return 2
    try: profile=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: print(f"PROFILE INVALID: {exc}"); return 2
    errors=validate(profile)
    if errors:
        print("PROFILE FAIL"); [print(f"- {e}") for e in errors]; return 1
    print("PROFILE PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
