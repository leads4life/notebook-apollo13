# APOLLO 13: THE LONG WAY HOME
A self-contained, original, headless Blender 5.2-LTS-targeted historical short pipeline. The 28-shot edit is 1,800 frames / 75 seconds at 24 fps; FINAL is 1920×1080 H.264/AAC assembled from lossless PNG frames.

## Local headless run
```bash
cd apollo13_blender
blender --background --python scripts/build_all.py
python3 scripts/create_audio.py
python3 scripts/validate_project.py --after-build
python3 scripts/render_all.py --profile PREVIEW
python3 scripts/assemble_video.py --profile PREVIEW --output previews/apollo13_full_animatic.mp4
# only after staged review:
python3 scripts/render_all.py --profile FINAL
python3 scripts/assemble_video.py --profile FINAL
```
`render_all.py` opens each scene independently. `render_shot.py --shot S01_PAD_REVEAL --profile REVIEW` supports targeted retries/ranges when invoked through Blender. The default procedural fallback has no network or paid dependency.

## Deliverables
- `production_manifest.json`: editorial, camera, asset, lighting, cost, and history metadata.
- `scripts/`: idempotent procedural model, scene, render, audio, validation, and assembly scripts.
- `colab/Apollo13_Blender_Render.ipynb`: mandatory staged test and approval workflow.
- `docs/`: historical notes, source policy, storyboard, render and recovery guides.

FINAL render demand is intentionally conservative but material: estimate 160 Cycles samples × 1,800 1080p frames; budget roughly 20–80 GPU-hours or considerably more on CPU, plus 30–100 GB for PNG frames depending on scene entropy. Run the five-frame final-quality test before committing compute.

## Google Colab from GitHub
Push the repository to GitHub, open `colab/Apollo13_Blender_Render.ipynb` in Colab, and use cell 3's Repository setup dialog to paste your HTTPS GitHub clone URL and select the branch. The cell validates the repository and automatically locates either a project-root layout or this repository's `apollo13_blender/` subdirectory.
