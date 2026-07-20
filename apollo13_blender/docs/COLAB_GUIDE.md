# Colab guide

1. Push this repository to GitHub, then open `colab/Apollo13_Blender_Render.ipynb` in Google Colab.
2. In notebook cell 3, a **Repository setup** dialog appears. Paste the HTTPS **clone URL** from GitHub's **Code** button (for example, `https://github.com/account/repository.git`), set the branch, and click **Clone / update repository**. Wait for the `Ready` message before continuing.
3. Run cells in their displayed order. The dialog performs a shallow clone on first run and fetches/checks out the requested branch on later runs. It accepts either a repository whose root is the Blender project or this repository's `apollo13_blender/` subdirectory layout.
4. Four preview approval booleans and the final-quality approval deliberately default to `False`; the final cell raises `FINAL RENDER BLOCKED` until all are explicitly changed to `True`.

For disconnect resilience, set `USE_DRIVE = True` in the first cell before cloning so frames and outputs can be preserved under Drive.
