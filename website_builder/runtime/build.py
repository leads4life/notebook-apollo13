#!/usr/bin/env python3
from pathlib import Path
import argparse, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

def resolve_mode(spec, override):
    if override and override != 'auto':
        return override
    requested = str(spec.get('mode','auto')).lower()
    if requested in {'original','retrofit'}:
        return requested
    if spec.get('approved_reference') or spec.get('retrofit_baseline'):
        return 'retrofit'
    return 'original'

def main():
    ap = argparse.ArgumentParser(description='Business Website Composer R3')
    ap.add_argument('spec')
    ap.add_argument('--output', required=True)
    ap.add_argument('--mode', choices=['original','retrofit','auto'], default='auto')
    ap.add_argument('--self-contained', action='store_true')
    args = ap.parse_args()
    spec_path = Path(args.spec).resolve()
    spec = json.loads(spec_path.read_text())
    mode = resolve_mode(spec, args.mode)
    script = ROOT/'runtime'/('build_original.py' if mode == 'original' else 'build_retrofit.py')
    cmd = [sys.executable, str(script), str(spec_path), '--output', str(Path(args.output).resolve())]
    if args.self_contained:
        cmd.append('--self-contained')
    print(f'R3 route: {mode.upper()}')
    raise SystemExit(subprocess.call(cmd))

if __name__ == '__main__':
    main()
