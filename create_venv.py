#!/usr/bin/env python3
"""Utility script to create a Python virtual environment.

Usage:
    python create_venv.py [venv_dir]

If no directory is provided, a folder named "venv" will be created in the current working directory.
"""

import sys
import os
import venv

def create_venv(target_dir: str):
    """Create a virtual environment at the given directory.

    Args:
        target_dir: Path to the directory where the venv will be created.
    """
    os.makedirs(target_dir, exist_ok=True)
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(target_dir)
    print(f"Virtual environment created at: {os.path.abspath(target_dir)}")
    if os.name == "nt":
        activate_path = os.path.join(target_dir, "Scripts", "activate")
        print(f"To activate, run: {activate_path}")
    else:
        activate_path = os.path.join(target_dir, "bin", "activate")
        print(f"To activate, run: source {activate_path}")

def main():
    venv_dir = sys.argv[1] if len(sys.argv) > 1 else "venv"
    create_venv(venv_dir)

if __name__ == "__main__":
    main()
