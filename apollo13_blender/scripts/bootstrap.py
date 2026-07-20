"""Headless entrypoint: blender --background --python scripts/bootstrap.py -- --profile PREVIEW"""
from build_all import main
from utilities import ensure_dirs
if __name__=='__main__':ensure_dirs();main()
