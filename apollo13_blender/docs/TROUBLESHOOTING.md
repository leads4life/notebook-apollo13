# Troubleshooting
- **No Blender/GPU:** set `BLENDER_EXECUTABLE`, use CPU fallback, or run the notebook pinned Blender install cell.
- **A shot fails:** inspect `logs/`, rerun `python scripts/render_all.py --profile REVIEW --shot Sxx_NAME`.
- **Missing frames:** rerun the same command; existing valid PNGs are skipped. Assembly deliberately fails rather than omitting a shot.
- **Out of memory:** lower REVIEW samples or run individual shots; retain FINAL profile values in source control and document any approved override.
