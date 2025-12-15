#!/usr/bin/env python3
from app import clean_name, normalize_name_for_comparison

cases = [
    ("ا_ محمد", "محمد"),
    ("أ_محمد", "محمد"),
    ("ا: محمد", "محمد"),
    ("أ:محمد", "محمد"),
    ("ا- محمد", "محمد"),
    ("ا-محمد", "محمد"),
    ("أ-محمد", "محمد"),
    ("أ: د. احمد", "احمد"),
    ("_احمد_", "احمد"),
]

failed = False
for inp, expected in cases:
    out = clean_name(inp)
    if out != expected:
        print(f"FAIL: '{inp}' -> '{out}' (expected '{expected}')")
        failed = True
    else:
        print(f"OK:   '{inp}' -> '{out}'")

# Test normalization
n = normalize_name_for_comparison('أحمد')
if n != 'احمد':
    print(f"FAIL normalize: 'أحمد' -> '{n}' (expected 'احمد')")
    failed = True
else:
    print("OK normalize: 'أحمد' -> 'احمد'")

if failed:
    print('\nSome tests failed')
    raise SystemExit(1)
else:
    print('\nAll tests passed')
