# Render guide
```bash
blender --background --python scripts/build_all.py
python3 scripts/create_audio.py
python3 scripts/validate_project.py --after-build
python3 scripts/render_all.py --profile PREVIEW
python3 scripts/assemble_video.py --profile PREVIEW --output previews/apollo13_full_animatic.mp4
```
Use `--profile FINAL` only after the staged Colab approvals. Frames are PNG sequences under `frames/<PROFILE>/<SHOT>/`; rendering skips valid files (>1 KiB), making it resumable. Assembly refuses missing frames.

## Visual QC
- [ ] Saturn V, CSM/LM, Moon, Earth, parachutes read clearly at shot scale.
- [ ] No crushed blacks, clipping, flickering, black/transparent frames, or unstable denoising.
- [ ] Instrument information is legible; no accidental celebrity likenesses.
- [ ] Space venting is gas/debris, never fire; exterior sound is bridged, not literal vacuum sound.
- [ ] Motion, focus, title cards, durations, and transitions are intentional.
