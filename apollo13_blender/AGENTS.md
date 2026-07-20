# Apollo 13 Blender Project Rules
- Prioritize successful automated, headless rendering; never require GUI interaction.
- Preserve deterministic output: fixed seeds, relative paths, idempotent builders.
- Do not silently omit failed shots; fail with actionable errors and write logs.
- Do not introduce undocumented dependencies or replace final assets with unexplained placeholders.
- Test every generated scene, preserve historical notes and render profiles.
- Optimize camera-visible quality first; keep all scripts rerunnable.
